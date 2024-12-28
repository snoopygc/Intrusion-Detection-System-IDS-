import os

def create_log_file(log_path):
    """
    Ensures log files exist; if not, create them.
    """
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    if not os.path.exists(log_path):
        with open(log_path, "w") as file:
            file.write("")
