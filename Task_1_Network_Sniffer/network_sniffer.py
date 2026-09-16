from scapy.all import sniff, IP, TCP, UDP, ICMP


def packet_callback(packet):
    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = packet[IP].proto

        print("\n-----------------------------")
        print(f"Source IP       : {source}")
        print(f"Destination IP  : {destination}")
        print(f"Protocol        : {protocol}")

        if TCP in packet:
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print(f"Source Port     : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")


print("===================================")
print("       BASIC NETWORK SNIFFER")
print("===================================")
print("Capturing packets...")
print("Press Ctrl+C to stop.\n")

sniff(prn=packet_callback, store=False)
