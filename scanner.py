import socket
import threading
import queue
import argparse


# FIELDS
threads = []

q = queue.Queue()

# add parser
parser = argparse.ArgumentParser(description="A multi-threaded port scanner")
parser.add_argument("target", help="The IP address to scan")
parser.add_argument("--ports", help='Port range to scan (e.g., 1-100)', default='1-1000')

args = parser.parse_args()
address = args.target

if '-' in args.ports:
    portParts = args.ports.split('-')
    portRange = range(int(portParts[0]),int(portParts[1]) + 1)
else:
    portRange = range(int(args.ports), int(args.ports) + 1)
    

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

def worker():
    while True:
        try:
            currentPort = q.get_nowait()
            scan(address, currentPort)
            q.task_done()
        except:
            break

# filling queue with ports
for p in portRange:
    q.put(p)

# initializing workers
for i in range(50):
    t = threading.Thread(target=worker)
    t.daemon = True # ends threading if program exits
    t.start()
    
# await scanning completion
q.join()
print('\nScanning complete.')


