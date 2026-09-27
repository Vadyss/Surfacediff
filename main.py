from cli import parser_args
from storage import get_scan_targets
from Ports.port_list import ports

from scanner import PortScanning

import asyncio

args = parser_args() # Starting CLI commands

"""Saving CLI commands output value"""
target_ip = args.target
output_file = args.output
detailed_console = args.verbose

if detailed_console:
    print(f"Scanning {target_ip}, saving to {output_file}") # Logging
    
ips_for_scan = get_scan_targets(target_ip, detailed_console) # Calling function for list of ips for scan

async def main(async_scans_at_one):
    semaphore = asyncio.Semaphore(async_scans_at_one)
    tasks = []
    
    for ip in ips_for_scan:
        for port in ports:
            tasks.append(asyncio.create_task(scan_ports(ip, port, semaphore)))

async def scan_ports(ip, port, semaphore):
    scan = PortScanning()
    
    async with semaphore:
        await scan.connect(ip, port)