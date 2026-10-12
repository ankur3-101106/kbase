---
title: Cross-Platform Notes & Environment Workflow
type: concept
area: systems
topics:
  - systems
  - cross-platform
  - git
  - markdown
status: evergreen
created: 2026-10-12
updated: 2026-10-12
---

# Cross-Platform Notes & Environment Workflow

## 1. Context & Objective
Operating a knowledge base across **Windows 11**, **Arch Linux**, and **Android (Termux)** introduces cross-platform edge cases: line ending mismatches, path separators, case-sensitivity discrepancies, and mobile editor limitations. This note documents the operational strategies enforced in `kbase` to ensure seamless interoperability.

---

## 2. Platform Comparison Matrix

| Property | Windows 11 | Arch Linux | Android (Termux / Markor) |
| :--- | :--- | :--- | :--- |
| **Primary Shell** | Git Bash / PowerShell 5.1 | Bash / Zsh | Termux Bash |
| **File System** | NTFS | Btrfs / Ext4 | F2FS / ext4 (via Android SAF) |
| **Case Sensitivity** | Case-Insensitive | Case-Sensitive | Case-Sensitive (under Termux root) |
| **Default Line Ending** | CRLF (`\r\n`) | LF (`\n`) | LF (`\n`) |
| **Path Separators** | Backslash (`\`) & Slash (`/`) | Slash (`/`) | Slash (`/`) |
| **Sync Automation** | Task Scheduler + `kbase-sync.sh` | Git CLI / systemd timer | Termux Cron / Tasker |

---

## 3. Core Interoperability Standards

### 3.1 Line Ending Normalization (`LF`)
- **Problem:** If Windows commits CRLF line endings, every line may appear modified in Linux or Git diffs, leading to false merge conflicts.
- **Solution:** Enforce LF in repository root `.gitattributes`:
  ```text
  * text=auto eol=lf
  *.md text eol=lf
  *.sh text eol=lf
  ```
  And configure `.editorconfig`:
  ```ini
  [*]
  end_of_line = lf
  charset = utf-8
  ```

### 3.2 Path Separators in Markdown
- **Rule:** **Never use Windows backslashes (`\`) inside Markdown links.**
- Markdown renderers (GitHub, Markor, Obsidian) interpret forward slashes (`/`) universally.
- ✅ Correct: `[SOP](../../procedures/synchronization-and-conflict-resolution.md)`
- ❌ Broken on Linux/Android: `[SOP](..\..\procedures\synchronization-and-conflict-resolution.md)`

### 3.3 Case Collisions & Naming Hygiene
- **Problem:** On Arch Linux, `Note.md` and `note.md` are distinct files. On Windows NTFS, Git cannot check out both simultaneously, producing checkout errors.
- **Rule:** All file and folder names must be strictly **lowercase and hyphenated** (`kebab-case.md`).
- **Forbidden Windows Characters:** Never use `< > : " / \ | ? *` in note filenames.

---

## 4. Environment-Specific Tips

### Windows 11 (Git Bash & Task Scheduler)
- Scheduled task executes:
  `"C:\Program Files\Git\bin\bash.exe" --login -i -c "bash /c/Users/Ankur/scripts/kbase-sync.sh"`
- Log output is kept in `C:\Users\Ankur\AppData\Local\KBaseSync\sync.log`.

### Arch Linux (Terminal & Ripgrep)
- Quick search shortcut in `.bashrc` or `.zshrc`:
  ```bash
  kb() {
    rg -i "$@" ~/kbase/knowledge ~/kbase/procedures
  }
  ```

### Android (Termux & Markor)
- In Markor, set repository directory to `kbase`.
- Keep quick notes minimal in `inbox/` so you do not need to manage folder navigation while on mobile.
