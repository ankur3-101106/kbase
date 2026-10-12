---
title: "SOP: <Procedure Title>"
type: procedure
area: procedures
topics:
  - <topic-1>
  - sop
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# SOP: <Procedure Title>

## 1. Purpose & Scope
- **Objective:** Clearly state what this procedure accomplishes.
- **Audience / Trigger:** Who executes this and under what operational conditions (e.g., weekly maintenance, onboarding new machine, disaster recovery).
- **Estimated Duration:** e.g., 15 minutes.

## 2. Prerequisites & Requirements
- **Privileges:** Root / `sudo` / Administrator / standard user.
- **Required Tools:** `rsync`, `git`, `gpg`, `btrfs-progs`.
- **Target Systems:** Arch Linux 6.x / Windows 11.

## 3. Step-by-Step Procedure

### Step 1: Pre-Execution Verification & Backup
Ensure the system is in a clean, backed-up state before modifying files.

```bash
# Verify current state
systemctl status target-service
```

### Step 2: Main Execution
Execute the core operations sequentially:

```bash
# Primary command
sudo command-step-one --option value
```
- **Expected Output:**
  ```text
  Successfully executed step 1.
  ```

```bash
# Secondary command
sudo command-step-two
```

### Step 3: Post-Execution Verification
Confirm the system has reached the desired end state:

```bash
# Health check
curl -f http://localhost:8080/health
```

## 4. Rollback & Contingency Plan
If any step fails or verification returns an error, execute this rollback sequence:

```bash
# Abort and restore previous configuration
sudo systemctl stop target-service
sudo cp /etc/backup/config.conf /etc/config.conf
sudo systemctl restart target-service
```

## 5. References & Change History
- Author / Maintainer: Ankur
- Related SOPs: [`[Troubleshooting Record]`](troubleshooting-record.md)
