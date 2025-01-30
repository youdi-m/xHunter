import scapy.all as scapy

class NetworkScanner:
    def __init__(self, target):
        self.target = target
    
    def discover_hosts(self):
        """ARP-based network discovery"""
        arp = scapy.ARP(pdst=self.target)
        ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        
        result = scapy.srp(packet, timeout=3, verbose=0)[0]
        return [{'ip': recv.psrc, 'mac': recv.hwsrc} for sent, recv in result]