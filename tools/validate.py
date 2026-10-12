#!/usr/bin/env python3
"""
kbase Validator
----------------
A lightweight, zero-dependency validation script for personal knowledge bases.
Checks:
  1. Broken relative Markdown links
  2. YAML frontmatter syntax and taxonomy conformance
  3. Case-insensitive filename collisions and Windows-incompatible filenames
  4. Accidentally staged secrets, private keys, or credentials heuristics

Requirements: Python 3.8+ (Standard Library only - zero pip dependencies)
Usage:
  python tools/validate.py
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

# Allowed taxonomy values
ALLOWED_TYPES = {
    "concept",
    "reference",
    "procedure",
    "troubleshooting",
    "lab",
    "study-note",
    "project",
    "resource",
    "decision",
    "capture",
}

ALLOWED_STATUSES = {
    "inbox",
    "draft",
    "active",
    "evergreen",
    "needs-review",
    "archived",
}

ALLOWED_AREAS = {
    "cybersecurity",
    "systems",
    "education",
    "programming",
    "procedures",
    "projects",
    "resources",
    "personal",
    "reference",
    "meta",
}

# Regex heuristics for potential secrets
SECRET_PATTERNS = [
    (re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"), "Private Key block"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS Access Key ID"),
    (re.compile(r"\bghp_[A-Za-z0-9]{36}\b"), "GitHub Personal Access Token"),
    (re.compile(r"\bgithub_pat_[A-Za-z0-9_]{82}\b"), "GitHub Fine-Grained Token"),
    (re.compile(r"\bxox[baprs]-[0-9a-zA-Z]{10,48}\b"), "Slack Token"),
]

# Windows forbidden filename characters: < > : " / \ | ? *
WINDOWS_FORBIDDEN_CHARS = set('<>:"/\\|?*')

# Directories to skip entirely during scanning
EXCLUDED_DIRS = {".git", ".idea", ".vscode", "__pycache__", "node_modules", "dist", "build"}


class KBaseValidator:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.errors = []
        self.warnings = []
        self.checked_files = 0
        self.checked_links = 0

    def log_error(self, file_path: Path, message: str):
        rel = file_path.relative_to(self.root_dir).as_posix()
        self.errors.append(f"[ERROR] {rel}: {message}")

    def log_warning(self, file_path: Path, message: str):
        rel = file_path.relative_to(self.root_dir).as_posix()
        self.warnings.append(f"[WARN]  {rel}: {message}")

    def validate_filenames(self, all_files):
        """Check for Windows forbidden characters and case collisions."""
        seen_lower = {}
        for f in all_files:
            rel = f.relative_to(self.root_dir)
            name = f.name

            # Check Windows forbidden characters
            for c in WINDOWS_FORBIDDEN_CHARS:
                if c in name:
                    self.log_error(f, f"Filename contains illegal Windows character: '{c}'")

            # Check case-collision
            lower_rel = rel.as_posix().lower()
            if lower_rel in seen_lower:
                self.log_error(f, f"Case collision with '{seen_lower[lower_rel]}'")
            else:
                seen_lower[lower_rel] = rel.as_posix()

    def parse_frontmatter(self, content: str):
        """Simple YAML frontmatter parser without yaml module."""
        if not content.startswith("---"):
            return None, content

        parts = content.split("---", 2)
        if len(parts) < 3:
            return None, content

        raw_yaml = parts[1].strip()
        body = parts[2]
        data = {}

        for line in raw_yaml.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip().strip("'\"")
                if key:
                    data[key] = val

        return data, body

    def check_frontmatter(self, file_path: Path, data: dict):
        """Validate taxonomy values if frontmatter is supplied."""
        if not data:
            return

        is_template = "templates" in file_path.parts

        note_type = data.get("type")
        if note_type and not (is_template and "<" in note_type) and note_type not in ALLOWED_TYPES:
            self.log_warning(
                file_path,
                f"Unknown type '{note_type}'. Allowed: {', '.join(sorted(ALLOWED_TYPES))}",
            )

        status = data.get("status")
        if status and not (is_template and "<" in status) and status not in ALLOWED_STATUSES:
            self.log_warning(
                file_path,
                f"Unknown status '{status}'. Allowed: {', '.join(sorted(ALLOWED_STATUSES))}",
            )

        area = data.get("area")
        if area and not (is_template and "<" in area) and area not in ALLOWED_AREAS:
            self.log_warning(
                file_path,
                f"Unknown area '{area}'. Allowed: {', '.join(sorted(ALLOWED_AREAS))}",
            )

    def check_secrets(self, file_path: Path, content: str):
        """Check for potential accidental secrets."""
        for pattern, desc in SECRET_PATTERNS:
            if pattern.search(content):
                self.log_error(file_path, f"Potential secret detected: {desc}")

    def check_markdown_links(self, file_path: Path, content: str):
        """Check relative links inside markdown."""
        is_template = "templates" in file_path.parts

        # Strip fenced code blocks
        clean_content = re.sub(r"```[\s\S]*?```", "", content)
        clean_content = re.sub(r"~~~[\s\S]*?~~~", "", clean_content)
        # Strip inline code spans
        clean_content = re.sub(r"`[^`\n]+`", "", clean_content)

        # Match standard Markdown links: [text](target)
        # Exclude images that start with ![
        link_pattern = re.compile(r"(?<!\!)\[(?P<text>[^\]]*)\]\((?P<target>[^\)]+)\)")

        for match in link_pattern.finditer(clean_content):
            target = match.group("target").strip()
            self.checked_links += 1

            # Skip web URLs, mailto, anchor-only links
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue

            # Skip template placeholders like <...>
            if is_template and ("<" in target or ">" in target):
                continue
            if "<" in target or ">" in target:
                continue

            # Strip anchor if present
            file_target = target.split("#", 1)[0]
            if not file_target:
                continue

            # Unquote URL encoding
            clean_target = unquote(file_target)

            # Check for Windows backslashes in markdown links
            if "\\" in clean_target:
                self.log_warning(
                    file_path,
                    f"Link uses Windows backslash: '{target}'. Use forward slashes.",
                )
                clean_target = clean_target.replace("\\", "/")

            # Resolve target path relative to current file's directory
            resolved_path = (file_path.parent / clean_target).resolve()

            if not resolved_path.exists():
                self.log_error(
                    file_path,
                    f"Broken link '{target}' -> Target does not exist ({resolved_path.name})",
                )

    def run(self) -> int:
        if hasattr(sys.stdout, "reconfigure"):
            try:
                sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

        print("[*] Starting kbase validation...\n")

        all_files = []
        md_files = []

        for root, dirs, files in os.walk(self.root_dir):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
            for f in files:
                full_path = Path(root) / f
                all_files.append(full_path)
                if f.endswith(".md"):
                    md_files.append(full_path)

        self.validate_filenames(all_files)

        for md_file in md_files:
            self.checked_files += 1
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception as e:
                self.log_error(md_file, f"Failed to read file as UTF-8: {e}")
                continue

            # Frontmatter check
            data, body = self.parse_frontmatter(content)
            self.check_frontmatter(md_file, data)

            # Secrets check
            self.check_secrets(md_file, content)

            # Link check
            self.check_markdown_links(md_file, content)

        # Print results
        print(f"[+] Summary:")
        print(f"    Files Scanned:   {self.checked_files}")
        print(f"    Links Checked:   {self.checked_links}")
        print(f"    Warnings:        {len(self.warnings)}")
        print(f"    Errors:          {len(self.errors)}")
        print("-" * 50)

        if self.warnings:
            print("\n[!] Warnings:")
            for w in self.warnings:
                print(f"    {w}")

        if self.errors:
            print("\n[-] Errors:")
            for e in self.errors:
                print(f"    {e}")
            print("\n[-] Validation FAILED.")
            return 1

        print("\n[+] All validation checks PASSED cleanly!")
        return 0


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    validator = KBaseValidator(root)
    sys.exit(validator.run())
