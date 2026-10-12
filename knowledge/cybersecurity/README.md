# Cybersecurity Knowledge Library (`knowledge/cybersecurity/`)

Reference material, core security concepts, offensive methodologies, and defensive frameworks.

---

## 📂 Sub-disciplines

### 🔬 [DFIR (Digital Forensics & Incident Response)](dfir/)
Investigation methodologies, artifact analysis (Windows Event Logs, Prefetch, Amcache, MFT, Linux syslog/auditd), memory forensics, and containment frameworks.
- **[DFIR Investigation Fundamentals](dfir/dfir-investigation-fundamentals.md)** — Core principles: RFC 3227 order of volatility, chain of custody, timeline analysis, and artifact triage.

### 🌐 Networking Security
Protocol weaknesses, firewall engineering, IDS/IPS tuning, deep packet inspection, TLS/SSL auditing, and network segmentation.

### 🕸️ Web Security
OWASP Top 10 vulnerabilities, authentication flaw analysis, OAuth/OIDC attack paths, business logic bypasses, and secure coding practices.

### 🎯 Penetration Testing
Active directory exploitation paths, privilege escalation methodologies, pivoting techniques, and post-exploitation.

### 🔍 Security Research
Vulnerability research, reverse engineering, exploit analysis, and proof-of-concept dissection.

---

## 🔒 Security Standards Reminder
- Never commit actual client data, confidential casework evidence, non-public zero-days, or raw `.pcap`/`.mem` files.
- Use placeholders for IPs and domains: RFC 5737 (`192.0.2.1`) and RFC 2606 (`example.com`).
