import socket
from concurrent.futures import ThreadPoolExecutor

class PortScanner:
    def __init__(self, target):
        self.target = target
    
    # Creates a TCP socket with connection timeout and returns 0 if
    # connection is successful (port is open)
    def scan_port(self, port, timeout=1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((self.target, port))
                return port if result == 0 else None
        except:
            return None

    # Concurrent port scanner to check multple ports with threads
    def scan(self, ports, max_threads=100):
        # Basic input validation
        if not ports:
            raise ValueError("No ports specified")
        if max_threads < 1:
            raise ValueError("max_threads must be positive")
        
        # Progress tracking
        total_ports = len(list(ports))
        scanned = 0

        # Creates thread pool, maps scan_port function across all ports
        # then filters and returns only the open ports
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            results = list(executor.map(self.scan_port, ports))
        return [port for port in results if port is not None]
    
    def parse_ports(self, port_string):
        """Parse port range string into a list of ports.
        
        Args:
            port_string (str): Port range (e.g. '80,443' or '1-1024')
        
        Returns:
            list: List of port numbers to scan
        """
        ports = []
        # Handle comma-separated ports
        for part in port_string.split(','):
            if '-' in part:
                # Handle range of ports
                start, end = map(int, part.split('-'))
                ports.extend(range(start, end + 1))
            else:
                # Handle single port
                ports.append(int(part))
        return sorted(list(set(ports)))