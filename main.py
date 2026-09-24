import sys
import os
from parser import parse_log_file
from analyzer import analyze_failed_logins
from report import generate_report

def main():
    # 1. Guard command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_log_file>")
        sys.exit(1)

    log_filename = sys.argv[1]

    # 2. Pipeline Execution
    raw_lines = parse_log_file(log_filename)
    metrics = analyze_failed_logins(raw_lines)
    generate_report(metrics, "system_report.txt")

if __name__ == "__main__":
    main()
