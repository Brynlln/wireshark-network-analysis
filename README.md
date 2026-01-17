## Wireshark Network Analysis

This project demonstrates hands-on network traffic analysis using Wireshark.
It includes real packet captures (PCAPs) and screenshots documenting protocol behavior.

### DNS Resolution Analysis
- Captured live DNS traffic over UDP port 53
- Identified standard DNS query structure and transaction IDs
- Observed FQDN resolution from domain name to IP address
- Analyzed protocol stack: Ethernet → IP → UDP → DNS

### Repository Structure
- pcaps/        Filtered packet capture files (.pcapng)
- screenshots/ Annotated screenshots from Wireshark analysis

### Tools Used
- Wireshark
- Windows

### Purpose
This project was created to demonstrate practical packet analysis skills
relevant to entry-level networking and cybersecurity roles.



### HTTP vs HTTPS Analysis
- Captured and compared unencrypted HTTP traffic and encrypted HTTPS traffic
- Observed plaintext HTTP requests including readable headers and URLs
- Verified HTTPS encryption using TLS, preventing inspection of application data
- Demonstrated why HTTPS protects confidentiality and integrity over HTTP

#### Key Observations
- HTTP traffic exposes request details in clear text
- HTTPS uses TLS to encrypt payloads, hiding content from packet inspection
- Protocol stack comparison: Ethernet → IP → TCP → HTTP vs TLS

#### Files
- pcaps/http-vs-https.pcapng
---

## Python PCAP Analysis (Scapy)

This repository also includes a Python-based PCAP analyzer built using **Scapy**.

**Script location:** `scripts/pcap_analyzer.py`

### What the script does
- Loads a PCAP file
- Counts DNS packets
- Identifies HTTP traffic (TCP port 80)
- Identifies HTTPS traffic (TCP port 443)

### Example Output


