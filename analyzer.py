def analyze_logs(logs):
    """
    Parses log lines, filters for 'FAILED', and calculates failure counts.
    """
    failed_counts = {}

    for line in logs:
        cleaned_line = line.strip()

        if "FAILED" in cleaned_line:
            parts = cleaned_line.split()

            # Safely handle malformed rows by ensuring enough parts exist
            if len(parts) > 3:
                # Index 3 gets the username right after "USER:"
                username = parts[3]

                if username in failed_counts:
                    failed_counts[username] += 1
                else:
                    failed_counts[username] = 1

    return failed_counts
