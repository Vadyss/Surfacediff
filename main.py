from cli import parser_args
from storage import get_scan_targets

args = parser_args() # Starting CLI commands

"""Saving CLI commands output value"""
target_ip = args.target
output_file = args.output
detailed_console = args.verbose

if detailed_console:
    print(f"Scanning {target_ip}, saving to {output_file}") # Logging
    
ips_for_scan = get_scan_targets(target_ip, detailed_console) # Calling function for list of ips for scan