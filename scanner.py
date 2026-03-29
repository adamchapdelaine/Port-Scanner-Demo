import socket

# FIELDS
address = '192.168.56.101'
port = 22

def scan(address, port):
    # INET, streaming socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # try TCP connection
    try:
        s.connect((address, port))
        print('Connected.')
    
    # exception if target port closed
    except:
        print('Not Connected.')
    
scan(address, port)    