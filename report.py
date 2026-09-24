import sys

def generate_report(failed_counts, output_file):
    """
    Writes formatted failed login metrics to an output file safely.
    """
    try:
        with open(output_file, "w") as report_file:
            for username, count in failed_counts.items():
                report_file.write(f"User: '{username}' | Count: '{count}'\n")
    except PermissionError:
        print(f"Error: Permission denied when attempting to write to '{output_file}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected issue occurred while creating '{output_file}': {e}")
        sys.exit(1)

    print(f"Report generated successfully at '{output_file}'.")

