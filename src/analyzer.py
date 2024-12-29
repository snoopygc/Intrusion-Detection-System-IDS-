import json
from src.alert import alert_user

def load_rules(file_path):
    """
    Loads signature rules from a JSON file.
    """
    with open(file_path, "r") as file:
        return json.load(file)

def analyze_packet(packet_data, rules):
    """
    Analyze packet to see if it matches any of the rules.
    """
    print(f"Analyzing Packet Data: {packet_data}")  # Debug: show payload data being analyzed
    for rule in rules:
        print(f"Checking Rule ID {rule['id']} with pattern '{rule['pattern']}'")  # Debug: show current rule
        if rule['pattern'].lower() in packet_data.lower():  # Check for pattern match in packet data
            print(f"Match found! Pattern '{rule['pattern']}' matched!")  # Debug: indicate match found
            alert_user(rule['pattern'], rule)  # Trigger the alert if a match is found
            return True, rule
    print("No rule matched for this packet.")  # Debug: no match
    return False, None
