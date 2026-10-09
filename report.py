import json
import csv

def generate_report(summary_data, output_path, format_type):
    if format_type == "json":
        with open(output_path, "w") as f:
            json.dump(summary_data, f, indent=4)
        print(f"[+] Successfully exported JSON report to: {output_path}")

    elif format_type == "csv":
        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Username", "Failed_Attempts"])
            for user, count in summary_data.items():
                writer.writerow([user, count])
        print(f"[+] Successfully exported CSV report to: {output_path}")

