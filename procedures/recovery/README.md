# Disaster Recovery & Rollback Procedures (`procedures/recovery/`)

Runbooks for disaster recovery, restoring notes from Git history, rolling back bad rebases, and recovering lost work.

---

## 📑 Core Recovery Procedures

### 1. Recovering from an Accidental Note Deletion
Git tracks the complete history of every commit. If a note was accidentally deleted:

```bash
# Find the commit where the file was deleted or last existed
git log --diff-filter=D --summary

# Restore the deleted file from the commit immediately prior
git checkout <commit-hash>^ -- path/to/deleted-note.md

# Stage and commit the restored file
git add path/to/deleted-note.md
git commit -m "Restore deleted-note.md from commit <commit-hash>"
```

### 2. Recovering from a Disastrous Rebase or Reset
If an interactive rebase or reset caused loss of recent local commits:

```bash
# View the local repository reflog
git reflog

# Locate the HEAD state prior to the rebase (e.g., HEAD@{2})
# Restore repository state to that point:
git reset --hard HEAD@{2}
```

### 3. Cloning a Fresh Copy on a New Machine
If a workstation or phone is lost or wiped:

```bash
# Clone the repository
git clone https://github.com/ankur3-101106/kbase.git
cd kbase

# Verify gitattributes line endings
git checkout-index --force --all
```
