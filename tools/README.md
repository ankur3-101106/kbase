# Validation Tools (`tools/`)

Lightweight, zero-dependency maintenance utilities designed to ensure link integrity, taxonomy correctness, and hygiene without requiring third-party libraries or background servers.

---

## 🛠️ `validate.py`

A standalone Python 3 script that audits the entire knowledge base.

### Purpose
- **Broken Link Detection:** Recursively extracts every relative Markdown link (`[text](path.md)`) and verifies that the target file exists on disk.
- **Taxonomy Validation:** Checks YAML frontmatter for valid `type`, `status`, and `area` values defined in [`CONTRIBUTING.md`](../CONTRIBUTING.md).
- **Cross-Platform Filename Safety:** Detects case-collision hazards (which fail on Windows/Linux checkout) and Windows-illegal characters (`< > : " / \ | ? *`).
- **Secret & Credential Heuristics:** Scans for unredacted private keys, AWS access keys, GitHub tokens, and Slack tokens.

### Requirements
- **Python 3.8+**
- **Zero Dependencies:** Uses only Python's standard library (`pathlib`, `re`, `sys`, `os`, `urllib`). No `pip install` required.

### Usage
From repository root on Windows, Arch Linux, or Android (Termux):

```bash
python tools/validate.py
```

### Example Successful Output
```text
🔍 Starting kbase validation...

📊 Summary:
   Files Scanned:   25
   Links Checked:   42
   Warnings:        0
   Errors:          0
--------------------------------------------------

✅ All validation checks PASSED cleanly!
```

### Failure Handling & Exit Codes
- **Exit Code 0:** All checks passed.
- **Exit Code 1:** One or more errors found (broken links, case collisions, illegal characters, or detected secrets).
- Fix each reported error and re-run `python tools/validate.py` before committing.
