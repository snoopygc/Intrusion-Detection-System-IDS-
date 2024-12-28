def alert_user(message, log_file="data/logs/intrusion.log"):
    """
    Logs alerts to a file and prints them to the console.
    """
    print(f"[ALERT]: {message}")
    with open(log_file, "a") as file:
        file.write(message + "\n")
