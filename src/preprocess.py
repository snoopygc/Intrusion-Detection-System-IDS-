from scapy.all import TCP, IP

def preprocess_packet(packet):
    """
    Preprocess packet to extract relevant data (payload).
    """
    if packet.haslayer(TCP):  # Check for TCP layer
        # If the packet has a payload (data)
        payload = str(packet[TCP].payload)
        
        # Debug: print what we extracted
        print(f"Extracted Payload: {payload}")
        
        return payload
    return None  # No payload if it's not a TCP packet with data
