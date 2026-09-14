from cli import parser_args
from storage import get_scan_targets

args = parser_args()

target_ip = args.target
output_file = args.output
detailed_console = args.verbose

if detailed_console:
    print(f"Scanning {target_ip}, saving to {output_file}")
    
ips_for_scan = get_scan_targets()