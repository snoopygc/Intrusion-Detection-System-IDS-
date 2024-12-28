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
    INTERFACE = "en0"  # เปลี่ยนเป็นอินเทอร์เฟซที่ถูกต้อง
    packets = capture_packets(interface=INTERFACE, count=10)


    for packet in packets:
        print(f"Captured Packet: {packet.summary()}")  # เพิ่มบรรทัดนี้เพื่อดูทุกแพ็กเก็ตที่จับได้
    
    packet_data = preprocess_packet(packet)
    if packet_data:
        print(f"Preprocessed Packet Data: {packet_data}")  # ตรวจสอบข้อมูลที่ preprocess
    
        is_intrusion, rule = analyze_packet(packet_data, rules)
        if is_intrusion:
            alert_user(f"Rule matched: {rule['description']} (ID: {rule['id']})")
            print(f"Alert: Rule matched - {rule}")  # เพิ่ม log ใน Console

from scapy.all import IP, TCP, send

# สร้างแพ็กเก็ตที่มี Payload ตรงกับกฎใน `rules.json`
packet = IP(dst="127.0.0.1") / TCP(dport=80) / "mobile.events.data.microsoft.com"
send(packet)

def alert_user(message):
    print(f"ALERT: {message}")  # พิมพ์ alert ออกมาที่ console
    with open('data/logs/intrusion.log', 'a') as log_file:
        log_file.write(f"{message}\n")


if __name__ == "__main__":
    main()
