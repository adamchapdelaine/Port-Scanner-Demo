import socket

# FIELDS
address = '192.168.56.101'

def scan(address, port):
    # INET, streaming socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    # try TCP connection
    try:
        s.connect((address, port))
        print(f'[+] Port {port} is OPEN.')
    
    # exception if target port closed
    except:
        print(f'[-] Port {port} is CLOSED.')


portRange = range(20, 31)

# scans ports in range
for p in portRange:
    scan(address, p)    