---
title: "Troubleshooting: Git Sync Failures & Lock Issues"
type: troubleshooting
area: procedures
topics:
  - git
  - synchronization
  - troubleshooting
status: evergreen
created: 2026-10-12
updated: 2026-10-12
---

# Troubleshooting: Git Sync Failures & Lock Issues

## 1. Problem Overview
- **Issue:** Automated sync via `kbase-sync.sh` fails, logs errors to `C:\Users\Ankur\AppData\Local\KBaseSync\sync.log`, or skips executions.
- **Affected Systems:** Windows 11 Task Scheduler, Arch Linux Git, Android Termux.

---

## 2. Quick Triage Table

| Observed Error in Log / Terminal | Root Cause | Primary Fix |
| :--- | :--- | :--- |
| `Another sync appears to be running; skipping.` | Stale `.git/kbase-sync-lock` directory from an interrupted process. | Remove `.git/kbase-sync-lock`. |
| `fatal: Unable to create '.../.git/index.lock': File exists.` | Git crashed or was killed while staging files. | Remove `.git/index.lock`. |
| `Unfinished merge/rebase detected; stopping.` | A previous rebase or merge encountered conflicts and halted. | Inspect `git status`, resolve conflict markers, run `git rebase --continue`. |
| `error: failed to push some refs... [rejected - non-fast-forward]` | Remote repository contains commits not present locally. | Run `git pull --rebase origin main` then push. |
| `fatal: You are in 'detached HEAD' state.` | Checked out a commit directly instead of branch `main`. | Run `git checkout main`. |
| `Host key verification failed` / `Permission denied (publickey)` | SSH agent inactive or expired GitHub token. | Verify SSH key with `ssh -T git@github.com`. |

---

## 3. Detailed Diagnostic & Resolution Steps

### Issue 1: Stale Sync Lock (`kbase-sync-lock`)
**Symptom:**
Log shows:
```text
[2026-10-12 00:00:01] Another sync appears to be running; skipping.
```

**Diagnostic:**
Check if a lock exists in `.git/`:
```bash
ls -d "C:/Users/Ankur/kbase/.git/kbase-sync-lock"
```

**Resolution:**
Confirm no sync process or Git instance is currently executing:
```powershell
Get-Process -Name git, bash -ErrorAction SilentlyContinue
```
Remove the lock directory:
```powershell
Remove-Item -Path "C:\Users\Ankur\kbase\.git\kbase-sync-lock" -Force -Recurse
```

---

### Issue 2: Git `index.lock` Failure
**Symptom:**
```text
fatal: Unable to create '.../.git/index.lock': File exists.
Another git process seems to be running in this repository...
```

**Resolution:**
```powershell
Remove-Item -Path "C:\Users\Ankur\kbase\.git\index.lock" -Force -ErrorAction SilentlyContinue
```

---

### Issue 3: Unfinished Rebase Detected
**Symptom:**
Log reports:
```text
[2026-10-12 00:00:02] Unfinished merge/rebase detected; stopping.
```

**Diagnostic:**
```bash
git status
```

**Resolution:**
1. Check what is conflicted:
   ```bash
   git diff --name-only --diff-filter=U
   ```
2. Open each conflicted file, resolve markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Stage and continue:
   ```bash
   git add <resolved-file>
   git rebase --continue
   ```
4. Or abort to clean state:
   ```bash
   git rebase --abort
   ```

---

### Issue 4: Detached HEAD State
**Symptom:**
```text
Expected branch main; stopping.
```

**Resolution:**
```bash
# Check current state
git branch

# Switch back to main
git checkout main
```

---

## 4. Verification Check
After applying any fix, test the sync script manually:

```bash
bash "C:/Users/Ankur/scripts/kbase-sync.sh"
```

Confirm that the output in `sync.log` shows:
```text
=== KBase sync started ===
No local changes to commit.
Sync completed successfully.
```
