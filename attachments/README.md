# Media & Attachments (`attachments/`)

This directory stores static visual assets, architecture diagrams, and sanitized screenshots referenced within notes.

---

## 📌 Rules for Attachments

1. **File Naming:**
   - Always use lowercase, hyphenated names: `YYYY-MM-DD-description.png` or `topic-subtopic.png`.
   - Examples: `2026-10-12-btrfs-subvolumes.png`, `dfir-evidence-timeline.svg`.
2. **Compression & Size Limits:**
   - Keep individual images under **1 MB** (ideally < 300 KB).
   - Use PNG for diagrams/screenshots and JPG/WebP for photos.
   - Do not commit multi-gigabyte video or audio files.
3. **Strict OPSEC & Redaction:**
   - Always blur or black out API keys, passwords, email addresses, personal identifiers, and private IP addresses before saving screenshots.
   - Never place raw memory dumps, packet captures (`.pcap`), or binaries here.
4. **Referencing in Notes:**
   - Reference via relative Markdown links:
     ```markdown
     ![Btrfs Subvolume Diagram](../../attachments/2026-10-12-btrfs-subvolumes.png)
     ```
