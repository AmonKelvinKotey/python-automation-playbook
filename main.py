import argparse 
from parser import parse_log_file
from analyzer import analyze_failed_logins
from report import generate_report

# 1. Initialize Argument Parser
parser = argparse.ArgumentParser(description="Security Log Analyzer CLI Tool")

# 2. Add Arguments/Flags
parser.add_argument("-f", "--file", required=True, help="Path to the target log file")
parser.add_argument("-o", "--output", default="report.json", help="Destination path for generated report")
parser.add_argument("-fmt", "--format", choices=["json", "csv"], default="json", help="Output format (json or csv)")

# 3. Parse Arguments from CLI
args = parser.parse_args()

# 4. Pipeline Execution
raw_lines = parse_log_file(args.file)
metrics = analyze_failed_logins(raw_lines)
generate_report(metrics, args.output, args.format)
