def analyze_failed_logins(log_lines):
    """
    Parses log lines, filters for 'FAILED', and calculates failure counts per user.
    """
    failed_counts = {}

    for line in log_lines:
        cleaned_line = line.strip()

        if "FAILED" in cleaned_line:
            parts = cleaned_line.split()
            username = parts[3]  # Index 3 gets the username right after "USER:"

            if username in failed_counts:
                failed_counts[username] += 1
            else:
                failed_counts[username] = 1

    return failed_counts
