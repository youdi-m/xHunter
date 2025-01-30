import argparse
from .modules.network import NetworkScanner

def main():
    parser = argparse.ArgumentParser(
        prog="xHunter",
        description="Network Security Scanner"
    )
    
    subparsers = parser.add_subparsers(dest="command")
    
    # Network scan command
    scan_parser = subparsers.add_parser('scan', help='Network discovery')
    scan_parser.add_argument('target', help='IP range to scan')
    
    args = parser.parse_args()
    
    if args.command == 'scan':
        scanner = NetworkScanner(args.target)
        results = scanner.discover_hosts()
        print_results(results)

def print_results(devices):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

if __name__ == "__main__":
    main()