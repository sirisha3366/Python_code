import scapy.all as scapy

request = scapy.ARP()
print(request.summary())
print(request.show())
print(scapy.ls(scapy.ARP()))