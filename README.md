# Python Automation Playbook

## 🚀 Overview

Core automation repository featuring Python system scripts, shell utilities, custom Linux permissions, and cybersecurity development workflows. Designed with a robust modular software architecture, strict error handling, and automated CI/CD checks.

---

## 🏛️ Project Architecture & Modules

The repository is organized into a modular pipeline for system logging analysis and automation:

* **`main.py`**: Program entry point utilizing Python's `argparse` module to handle command-line flags (`--file` for log path specification and `--format` for output serialization type) and orchestrate the analysis pipeline.


* **`parser.py`**: Ingests log files line-by-line with robust EAFP (Easier to Ask for Forgiveness than Permission) exception handling, protecting against `FileNotFoundError` and `PermissionError`.


* **`analyzer.py`**: Processes log streams, filters lines for security events (such as `FAILED` attempts), safely extracts usernames, and aggregates failure counts.


* **`report.py`**: Formats and exports data summaries into structured files supporting both `json` and `csv` formats.



---

## 🛠️ System & Security Utilities

* **`system_info.py`**: A workspace inspection script leveraging Python's `platform` and `os` modules to query operating system releases, architectures, and current working directories.


* **`security_test.sh`**: A hardened executable shell script configured with strict `700` permissions for executing basic system security validation checks.



---

## ⚙️ CI/CD & Governance

* **GitHub Actions Workflow (`.github/workflows/lint.yml`)**: Automated workflow configured to enforce code quality, linting standards, and PEP 8 compliance on every push.


* **Engineering Logs (`DEBRIEF_WEEK4.md`)**: Comprehensive documentation tracking technical implementation lessons, refactoring milestones, and phase planning.


* **`.gitignore`**: Configured to safely exclude virtual environments (`.venv/`), Python byte code caches (`__pycache__/`), and local runtime outputs (`.log`, `.json`, `.csv`, `.save`).



---

## 📦 Installation & Usage

1. **Clone the repository:**
```bash
git clone https://github.com/AmonKelvinKotey/python-automation-playbook.git
cd python-automation-playbook

```


2. **Run the Log Analyzer CLI:**
```bash
python3 main.py --file /path/to/logfile.log --format json

```



---

## 📄 License

Distributed under the MIT License. See the repository for more details.
