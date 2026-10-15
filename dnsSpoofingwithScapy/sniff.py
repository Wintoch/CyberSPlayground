from scapy.all import ARP, Ether, send, sniff, IP
import data

def mainLoop(packet):
    if packet.haslayer(IP):
        return packet.summary()
    
sniff(iface="en0", filter=f"host {data.ipPhone}", prn=mainLoop, store=False)