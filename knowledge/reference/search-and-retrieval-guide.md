---
title: Search and Retrieval Guide for kbase
type: reference
area: reference
topics:
  - search
  - ripgrep
  - github
  - retrieval
status: evergreen
created: 2026-10-12
updated: 2026-10-12
---

# Search and Retrieval Guide for kbase

## 1. Overview & Strategy
A personal knowledge base succeeds or fails on the speed and reliability of information retrieval. Rather than maintaining brittle, manual index files that rot over time, `kbase` relies on:
1. **Descriptive, hyphenated filenames** (`kebab-case.md`).
2. **Clear Markdown headings** (`# H1`, `## H2`).
3. **Structured YAML frontmatter** (`type:`, `area:`, `status:`).
4. **Fast plain-text search tools** (`rg` locally, GitHub search remotely, Markor on mobile).

---

## 2. Local Search with Ripgrep (`rg`)

`ripgrep` is available on Arch Linux (`pacman -S ripgrep`), Windows (`winget install BurntSushi.ripgrep.MSVC`), and Android Termux (`pkg install ripgrep`).

### 2.1 Full-Text Search
```bash
# Case-insensitive search across all notes
rg -i "btrfs snapshot"

# Search only in knowledge directory
rg -i "heap overflow" knowledge/

# Show 2 lines of context around matches
rg -i -C 2 "order of volatility" knowledge/cybersecurity/
```

### 2.2 Heading & Title Search
Because note titles and sections use standard Markdown `#` headings:
```bash
# Find all notes containing a specific title or major heading
rg "^#+ .*DNS"

# List only top-level H1 titles
rg "^# " knowledge/
```

### 2.3 Frontmatter Metadata Filtering
Filter notes based on type, area, or lifecycle status:
```bash
# Find all Standard Operating Procedures
rg "^type: procedure"

# Find all notes marked as needs-review or draft
rg "^status: (needs-review|draft)"

# Find notes tagged with a specific topic
rg "^  - dfir" knowledge/
```

### 2.4 Filename Search
```bash
# List all notes matching a topic pattern
rg --files | rg "troubleshooting"

# Or using find / git
git ls-files "*sync*"
```

---

## 3. Shell Aliases for Faster Work

Add these functions to your `~/.bashrc` (Arch Linux / Git Bash / Termux) or PowerShell profile:

### Bash / Zsh (`~/.bashrc`)
```bash
# Fast knowledge base search
kb() {
  rg -i "$@" ~/kbase/knowledge ~/kbase/procedures ~/kbase/projects
}

# Fast heading search
kbh() {
  rg -i "^#+ .*$1" ~/kbase/
}

# Fast note filename lookup
kbf() {
  git -C ~/kbase ls-files "*$1*"
}
```

### PowerShell (`$PROFILE`)
```powershell
function kb { param([string]$q) rg -i $q "C:\Users\Ankur\kbase\knowledge", "C:\Users\Ankur\kbase\procedures" }
function kbh { param([string]$q) rg -i "^#+ .*$q" "C:\Users\Ankur\kbase" }
```

---

## 4. Searching on GitHub

When accessing `kbase` through the GitHub web interface:

1. **Quick File Finder:** Press `t` anywhere in the repository view to open GitHub's instant file search modal. Start typing keywords (e.g., `dfir`, `sync`, `cheatsheet`).
2. **Path-Scoped Code Search:** Use the search bar with path qualifiers:
   ```text
   repo:ankur3-101106/kbase path:knowledge/ "volatile memory"
   repo:ankur3-101106/kbase path:procedures/ "rebase conflict"
   ```
3. **Symbol & Heading Search:** GitHub's symbol search (`Ctrl+Shift+O` or outline view) allows instant jumping across headings.

---

## 5. Searching on Mobile (Android)

1. **Markor (App):**
   - Use the magnifying glass icon at the top of the folder view.
   - Searches filenames and note contents instantly offline.
2. **Termux (Terminal):**
   - Run `rg -i "search term" ~/kbase/` directly in Termux.
