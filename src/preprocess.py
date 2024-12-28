from scapy.all import Raw

def preprocess_packet(packet):
    if packet.haslayer(Raw):  # ถ้ามี Raw Layer ในแพ็กเก็ต
        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        print(f"Extracted Payload: {payload}")  # ให้แสดงผล Payload ที่ดึงออกมา
        return {"payload": payload}
    else:
        return None
