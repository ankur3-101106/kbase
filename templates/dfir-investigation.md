---
title: "DFIR Case Study: <Incident / Case Name>"
type: lab
area: cybersecurity
topics:
  - dfir
  - incident-response
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# DFIR Case Study: <Incident / Case Name>

## 1. Case Overview
- **Case Reference:** IR-YYYY-XXXX
- **Incident Category:** Ransomware / Account Compromise / Data Exfiltration / Malware Infection
- **Initial Detection Date/Time:** <YYYY-MM-DD HH:MM UTC>
- **Objective:** Determine initial access vector, lateral movement, persistence, and scope of impact.

## 2. Affected Scope & Assets
| Hostname | Role / OS | IP Address | Impact Level |
| :--- | :--- | :--- | :--- |
| `ws-01.internal` | Workstation / Win11 | `192.0.2.25` | Initial compromise |
| `srv-dc01.internal` | Active Directory / WinSrv | `192.0.2.5` | Targeted for credential dumping |

## 3. Evidence Artifacts & Chain of Custody
*(Raw forensic dumps must remain in local secure lab storage outside Git; store only hashes and metadata here.)*

| Artifact ID | Description | Source | SHA-256 Hash |
| :--- | :--- | :--- | :--- |
| `EVD-01` | Memory Image (`mem.raw`) | `ws-01` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `EVD-02` | Triage Zip (MFT, Logs) | `ws-01` | `ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb` |

## 4. Chronological Incident Timeline
| Timestamp (UTC) | Source / Artifact | Activity Observed | Attacker Technique (MITRE) |
| :--- | :--- | :--- | :--- |
| `2026-10-12 10:14:02` | Web Proxy Log | Phishing link clicked | Initial Access (T1566) |
| `2026-10-12 10:15:30` | Windows Event 4688 | `powershell.exe` spawned by Word | Execution (T1059.001) |
| `2026-10-12 10:20:11` | Security Event 4624 | Successful logon via stolen token | Lateral Movement (T1078) |

## 5. Artifact Analysis Details
- **Memory Analysis (Volatility):** Malicious process injected into `svchost.exe`.
- **MFT & File System:** Dropped payload located in `C:\Users\<USER>\AppData\Local\Temp\`.
- **Event Logs:** Security Event ID 4625 (brute force) followed by 4624 (type 3 network logon).

## 6. Indicators of Compromise (IOCs)
| Type | Value | Context |
| :--- | :--- | :--- |
| IPv4 | `198.51.100.45` | C2 Callback Server |
| Domain | `c2.malicious-example.com` | Staging domain |
| SHA-256 | `a1b2c3d4e5f6...` | Dropper payload |
| File Path | `C:\Windows\Temp\updater.exe` | Staged persistence binary |

## 7. Containment, Eradication & Recovery
1. **Network Isolation:** Host `ws-01` disconnected via firewall rule.
2. **Account Reset:** Compromised domain accounts forced password reset and MFA revocation.
3. **Eradication:** Scheduled task `SystemUpdater` removed; malicious registry run keys purged.

## 8. Root Cause & Lessons Learned
- **Root Cause:** Inadequate email attachment filtering allowed macro-enabled document execution.
- **Recommendations:** Implement Attack Surface Reduction (ASR) rules, block Office child process spawning, enforce FIDO2 MFA.
