---
title: "Checklist: Weekly Inbox Review & Repository Hygiene"
type: procedure
area: procedures
topics:
  - checklist
  - maintenance
  - inbox
status: evergreen
created: 2026-10-12
updated: 2026-10-12
---

# Checklist: Weekly Inbox Review & Repository Hygiene

Run this 10-minute maintenance checklist weekly to prevent inbox clutter, preserve accurate taxonomy, and keep cross-device synchronization healthy.

---

## Phase 1: Inbox Processing & Triage

- [ ] **1. List all captures:** Inspect files currently located in `inbox/`:
  ```bash
  ls -la inbox/
  ```
- [ ] **2. Triage each capture:**
  - If a note is a reusable concept: Move to `knowledge/<area>/<filename>.md`.
  - If a note is an actionable procedure: Move to `procedures/<subfolder>/<filename>.md`.
  - If a note belongs to an active project: Move to `projects/<project-name>/`.
  - If a note is ephemeral, completed, or no longer relevant: Delete it or move to `archive/`.
- [ ] **3. Apply standard frontmatter:** Ensure each moved note has `title`, `type`, `area`, `status`, and `created` fields.
- [ ] **4. Verify `inbox/` is clear:** Only `inbox/README.md` should remain.

---

## Phase 2: Active Note Review & Lifecycle Updates

- [ ] **1. Inspect drafts and notes needing review:**
  ```bash
  rg "^status: (draft|needs-review)"
  ```
- [ ] **2. Promote or archive:**
  - Completed drafts with verified contents ➡️ Change to `status: active` or `status: evergreen`.
  - Outdated procedures or decommissioned projects ➡️ Update `status: archived` and move to `archive/`.
- [ ] **3. Update cross-references:** Add relative links in `HOME.md` or parent index files if significant new notes were created.

---

## Phase 3: Automated Validation & Integrity Check

- [ ] **1. Run the local validation script:**
  ```bash
  python tools/validate.py
  ```
  - Verify zero broken relative links.
  - Verify frontmatter syntax is valid.
  - Verify no accidental secret patterns or credential files exist.
  - Verify no Windows-incompatible filenames or case collisions exist.
- [ ] **2. Check Git status:**
  ```bash
  git status
  ```
  Ensure all files are tracked and there are no unstaged changes or untracked debris.

---

## Phase 4: Sync Health Verification

- [ ] **1. Inspect the sync log on Windows:**
  ```powershell
  Get-Content "C:\Users\Ankur\AppData\Local\KBaseSync\sync.log" -Tail 20
  ```
- [ ] **2. Confirm clean upstream status:** Ensure `origin/main` is up to date and no rebase or merge locks are active.
