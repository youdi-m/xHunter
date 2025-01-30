import argparse
from .modules.network import NetworkScanner

def main():
    parser = argparse.ArgumentParser(
        prog="xHunter",
        description="Comprehensive Network Security Scanner"
    )
    
    subparsers = parser.add_subparsers(dest="command")
    
    # Network scan command parsers
    scan_parser = subparsers.add_parser('scan', help='Network discovery')
    scan_parser.add_argument('target', help='IP range to scan')

    # Port scan command parsers
    port_parser = subparsers.add_parser('portscan', help='Port scanning')
    port_parser.add_argument('target', help='Target IP')
    port_parser.add_argument('-p', '--ports', default='1-1024',
                            help='Port range (e.g., 1-100 or 80,443)')
    
    args = parser.parse_args()
    
    # Matching arguments
    match args.command:
        # NetworkScanner
        case 'scan':
            scanner = NetworkScanner(args.target)
            results = scanner.discover_hosts()
            print_results(results)
        # PortScanner
        case 'portscan':
            from .modules.ports import PortScanner
            scanner = PortScanner(args.target)
            ports = scanner.parse_ports(args.ports)
            open_ports = scanner.scan(ports)
            print(f"Open ports: {', '.join(map(str, open_ports))}")
        # Default
        case _:
            print("Unknown command. Use --help for usage information.")

# Results function for NetworkScanner
def print_results(devices):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

if __name__ == "__main__":
    main()