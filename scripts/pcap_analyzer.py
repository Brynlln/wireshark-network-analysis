from scapy.all import rdpcap, DNS, TCP

print("PCAP analyzer starting...\n")

# PCAP file must be in the same folder OR use a relative path
PCAP_FILE = "dns-resolution.pcapng"

packets = rdpcap(PCAP_FILE)

dns_count = 0
http_count = 0
https_count = 0

for pkt in packets:
    if pkt.haslayer(DNS):
        dns_count += 1

    if pkt.haslayer(TCP):
        if pkt[TCP].dport == 80 or pkt[TCP].sport == 80:
            http_count += 1

        if pkt[TCP].dport == 443 or pkt[TCP].sport == 443:
            https_count += 1

print("PCAP Analysis Results")
print("--------------------")
print(f"Total packets: {len(packets)}")
print(f"DNS packets: {dns_count}")
print(f"HTTP packets (port 80): {http_count}")
print(f"HTTPS packets (port 443): {https_count}")
