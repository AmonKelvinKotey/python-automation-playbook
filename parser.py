import sys

def parse_log_file(file_path):
    """
    Attempts to read a log file securely and returns its raw lines.
    """
    try:
        with open(file_path, "r") as log_file:
            lines = log_file.readlines()
            return lines
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
        
    except PermissionError:
        print(f"Error: Access denied for '{file_path}'. Permission missing.")
        sys.exit(1)
        
    except Exception as e:
        print(f"An unexpected error occurred while reading '{file_path}': {e}")
        sys.exit(1)    
