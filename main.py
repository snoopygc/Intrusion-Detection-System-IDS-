from src.capture import capture_packets
from src.preprocess import preprocess_packet
from src.analyzer import load_rules, analyze_packet
from src.alert import alert_user
from src.utils import create_log_file

def main():
    """
    Entry point for the IDS program.
    """
    # Load rules
    rules = load_rules("config/rules.json")

    # Prepare log files
    create_log_file("data/logs/intrusion.log")

    # Capture packets
    print("Starting packet capture...")
    INTERFACE = "en0"
    packets = capture_packets(interface=INTERFACE, count=10)


    for packet in packets:
        print(f"Captured Packet: {packet.summary()}")
    
    packet_data = preprocess_packet(packet)
    if packet_data:
        print(f"Preprocessed Packet Data: {packet_data}")
    
        is_intrusion, rule = analyze_packet(packet_data, rules)
        if is_intrusion:
            alert_user(f"Rule matched: {rule['description']} (ID: {rule['id']})")
            print(f"Alert: Rule matched - {rule}")

from scapy.all import IP, TCP, send

packet = IP(dst="127.0.0.1") / TCP(dport=80) / "mobile.events.data.microsoft.com"
send(packet)

def alert_user(message):
    print(f"ALERT: {message}")
    with open('data/logs/intrusion.log', 'a') as log_file:
        log_file.write(f"{message}\n")


if __name__ == "__main__":
    main()
