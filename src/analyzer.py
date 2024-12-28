import json
from src.alert import alert_user

def load_rules(file_path):
    """
    Loads signature rules from a JSON file.
    """
    with open(file_path, "r") as file:
        return json.load(file)

def analyze_packet(packet_data, rules):
    payload = packet_data.get('payload', '')  # รับ Payload ที่แยกออกมา
    print(f"Checking packet data: {payload}")  # ดูข้อมูลของแพ็กเก็ต
    for rule in rules:
        if rule['pattern'] in payload:  # ค้นหา pattern ที่ตรงกับ payload
            alert_user(f"ALERT: Pattern '{rule['pattern']}' detected (ID: {rule['id']})")
            print(f"Alert triggered for rule ID: {rule['id']}, description: {rule['description']}")
            return True, rule
    return False, None