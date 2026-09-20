import argparse
import ipaddress

def valid_target(value: str) -> ipaddress.IPv4Network: # Validation so only network can go thru
    try:
        network = ipaddress.ip_network(value, strict=False)
        return network
    except ValueError:
        raise argparse.ArgumentTypeError("IP address is not valid.")
    
def parser_args() -> argparse.Namespace: # Defining CLI commands
    parser = argparse.ArgumentParser(
        prog="Surfacediff",
        description="This program is for scanning open ports in network, and for what is that port used.",
    )

    parser.add_argument(
        '--target',
        help="IP address or CIDR range to scan (e.g. 192.168.1.0/24).",
        required=True,
        type=valid_target
    )

    parser.add_argument(
        '--output',
        help="Directory where the snapshot will be saved (default: ./snapshots/).",
        default="./snapshots/"
    )

    parser.add_argument(
        '--verbose', '-v',
        help="Show detailed output during the scan.",
        action="store_true"
    )

    return parser.parse_args()