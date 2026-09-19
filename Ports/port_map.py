probes = {
    # --- HTTP / HTTP-like ---
    3000: b"GET / HTTP/1.0\r\n\r\n",
    5000: b"GET / HTTP/1.0\r\n\r\n",
    5601: b"GET / HTTP/1.0\r\n\r\n",   # Kibana
    5984: b"GET / HTTP/1.0\r\n\r\n",   # CouchDB
    7001: b"GET / HTTP/1.0\r\n\r\n",
    8000: b"GET / HTTP/1.0\r\n\r\n",
    8081: b"GET / HTTP/1.0\r\n\r\n",
    8443: b"GET / HTTP/1.0\r\n\r\n",   # pozor, tady bude typicky TLS (viz poznámka níže)
    8888: b"GET / HTTP/1.0\r\n\r\n",
    9000: b"GET / HTTP/1.0\r\n\r\n",
    9090: b"GET / HTTP/1.0\r\n\r\n",
    9200: b"GET / HTTP/1.0\r\n\r\n",   # Elasticsearch
    2375: b"GET / HTTP/1.0\r\n\r\n",   # Docker API (bez TLS)
    2376: b"GET / HTTP/1.0\r\n\r\n",   # Docker API (typicky TLS)
    631:  b"GET / HTTP/1.0\r\n\r\n",   # CUPS/IPP
    81:   b"GET / HTTP/1.0\r\n\r\n",

    # --- Vlastní textové protokoly, jiný probe než GET ---
    2181: b"ruok\r\n",                 # Zookeeper four-letter command
    6379: b"PING\r\n",                 # Redis inline command

    # --- MongoDB — schválně zkoušíme HTTP, MongoDB na to odpoví čitelnou hláškou ---
    27017: b"GET / HTTP/1.0\r\n\r\n",

    # --- Binární protokoly — text pravděpodobně nic nepřinese, ale nechávám prázdné,
    #     ať connect() ví, že tu se aktivně nemá nic posílat ---
    389: b"",     # LDAP
    636: b"",     # LDAPS
    464: b"",     # Kerberos
    902: b"",     # VMware auth daemon
    1433: b"",    # MSSQL (má vlastní prelogin handshake)
    1521: b"",    # Oracle TNS
    2049: b"",    # NFS/RPC
    5432: b"",    # PostgreSQL (čeká binární startup packet)
    514: b"",     # syslog
    587: b"",     # SMTP submission — obvykle promluví sám (pasivně)
    1025: b"",    # ambiguous/RPC
}