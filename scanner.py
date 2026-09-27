import asyncio

from Ports.port_map import probes

class PortScanning:
    """Handles a single TCP connect + optional banner grab for one IP:port."""
    
    def __init__(self): # Defining values thru class
        self = self
    
    async def connect(self, ip, port) -> dict:
        """Try to open a TCP connection and grab a banner if possible."""
        banner = None
        
        write_msg = probes.get(self.port, b"")
        
        try:
            temp = asyncio.open_connection(ip, port)
            reader, writer = await asyncio.wait_for(temp, timeout=3)
        
        except ConnectionRefusedError: # Port is closed
            error_msg = {"status": "closed", "banner": None}
            return error_msg
        except (asyncio.TimeoutError, OSError): # Port timeout
            error_msg = {"status": "timeout", "banner": None}
            return error_msg
        
        try:
            data = await asyncio.wait_for(reader.read(1024), timeout=3)
            
            if data: # Server give first message
                banner = data.decode(errors="ignore")
            else: # We need to speek to the server
                if write_msg:
                    writer.write(write_msg)
                    await writer.drain()
                        
                    data = await asyncio.wait_for(reader.read(1024), timeout=3)
                    if data:    
                        banner = data.decode(errors="ignore")

        except (asyncio.TimeoutError, OSError): # Connection succeeded, banner grab failed
            pass 
        
        finally: # Closing connection
            writer.close()
            await writer.wait_closed()

        return {"status": "open", "banner": banner}