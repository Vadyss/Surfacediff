import http.client
import urllib
import socket
import asyncio

from Ports.port_list import ports
from main import ips_for_scan

class portScanning():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    async def connect(self) -> bool:
        try:
            temp = asyncio.open_connection(self.ip, self.port)
            result = await asyncio.wait_for(temp, timeout=3)
            return result
        except RuntimeError:
            return result
        
            