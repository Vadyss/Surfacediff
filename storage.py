import ipaddress

def get_scan_targets(target_ip: ipaddress.IPv4Network, detailed_console: bool) -> list: # List of ips for scan
    if isinstance(target_ip, ipaddress.IPv4Network):
        if detailed_console:
            print(f"Scanning detected {list(target_ip.hosts())} IPs")
        return list(target_ip.hosts())