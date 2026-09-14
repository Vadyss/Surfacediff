import ipaddress
from subnetcalc import Ip

from main import target_ip , detailed_console 

def get_scan_targets() -> list | str:
    if isinstance(target_ip, ipaddress.IPv4Address):
        if detailed_console:
            print(f"Scanning detected only {target_ip} IP")
        return target_ip
    elif isinstance(target_ip, ipaddress.IPv4Network):
        if detailed_console:
            print(f"Scanning detected {target_ip.available_ips} IPs")
        return list(target_ip.available_ips)