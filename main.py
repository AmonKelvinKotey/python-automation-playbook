import argparse
from analyzer import analyze_logs
from parser import parse_log_file
from report import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="Log Analysis and Reporting CLI Pipeline Tool"
    )
    parser.add_argument(
        "--file", required=True, help="Path to the log file to analyze"
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        default="json",
        help="Format for the output report (json or csv)",
    )
    args = parser.parse_args()

    logs = parse_log_file(args.file)
    summary = analyze_logs(logs)

    # Define the output filename based on the chosen format argument
    output_filename = f"report.{args.format}"

    generate_report(summary, output_filename, args.format)


if __name__ == "__main__":
    main()
