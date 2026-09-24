# Phase 1 — Week 4 Operational Debrief
**Date:** September 24, 2026  
**Focus:** Modular Pipeline Refactoring, EAFP Exception Safety, & Real Log Analysis  

---

## 1. Technical Accomplishments
* **Modular Pipeline Refactoring:** Successfully split the monolithic script into a 3-stage architecture:
  * `parser.py`: File ingestion and line reading.
  * `analyzer.py`: Keyword filtering (`"FAILED"`) and token extraction via index `parts[3]`.
  * `report.py`: File output formatting (`system_report.txt`).
  * `main.py`: Orchestrator handling dynamic CLI argument ingestion (`sys.argv`).
* **Defensive Error Handling (EAFP):** Wrapped file I/O operations in robust `try/except` blocks to handle `FileNotFoundError`, `PermissionError`, and generic `Exception` edge cases safely.
* **Live System Testing:** Verified script execution against live Crostini system logs (`/var/log/auth.log`) using `sudo` and confirmed `PermissionError` handling when executed as an unprivileged user.

---

## 2. Technical Engineering Lessons
* **Tokenization Anomalies:** Parsing non-standard log lines or arbitrary files (e.g., source code like `log_analyzer.py`) causes index targeting shifts where unexpected string tokens (such as `clean_line:`) are extracted as user names.
* **Log Structure Dependencies:** Real system log formats place timestamps and hostnames at indices 0–3, requiring regex or dynamic delimiter matching rather than fixed space indexing (`parts[3]`) for production log parsing.

---

## 3. Git Operations
* Staged and committed all core modules:
  * Commit ID: `342e323`
  * Message: `refactor(pipeline): implement modular 3-stage architecture and EAFP exception handling`

---

## 4. Next Objective (Week 5)
* Transition to **OverTheWire (OTW) Bandit** to build hands-on Linux system security, file permission navigation, and SSH operations mastery.
