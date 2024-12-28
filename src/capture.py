from scapy.all import sniff

def capture_packets(interface="eth0", count=0):
    """
    Captures packets from a specified network interface.
    """
    packets = sniff(iface=interface, count=count)
    return packets
