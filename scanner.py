import socket
import threading
import queue
import argparse

# FIELDS
MAX_THREADS = 100
TIMEOUT = 0.5

q = queue.Queue()
openPorts = []
lockPrint = threading.Lock()


def scan(address, port):
    # Create a socket object
    # AF_INET specifies IPv4 address family
    # SOCK_STREAM specifies TCP communication protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    try:
        # Attempt connection to target IP, port
        s.connect((address, port))
        # If successful, lock thread to safely add port to shared list
        with lockPrint:
            openPorts.append(port)

    except: # Log exception to file/console
        # If connection fails (port closed/timeout), ignore error and proceed
        pass


def worker(address):
    while True:
        try:
            # Safely grab next port from queue
            # get_nowait() prevents thread from freezing if empty
            currentPort = q.get_nowait()
            scan(address, currentPort)
            q.task_done()  # Signal to queue that port was processed
            print('.', end='', flush=True)  # flush=True prints live output
        except queue.Empty:
            # Exit loop when queue is emptied
            break


def main():
    threads = []

    # Initialize argument parser
    # Add mandatory positional argument for target IP
    # Add optional argument for port range + set default range
    parser = argparse.ArgumentParser(
        description='A multi-threaded port scanner')
    parser.add_argument('target', help='The IP address to scan')
    parser.add_argument(
        '--ports', help='Port range to scan (e.g., 1-100)', default='1-1000')

    # Parse arguments provided by user
    args = parser.parse_args()
    address = args.target

    print('Scanning...')

    # Logic to handle single port input (80) or range (20-30)
    if '-' in args.ports:
        portParts = args.ports.split('-')  # Split string by hyphen
        portRange = range(int(portParts[0]), int(
            portParts[1]) + 1)  # + 1 is inclusive
    else:
        # If no hyphen, treat input as single port
        portRange = range(int(args.ports), int(args.ports) + 1)

    # Fill queue with each port in range
    for p in portRange:
        q.put(p)

    # Spawn worker threads to concurrently process queue
    for i in range(MAX_THREADS):
        t = threading.Thread(target=worker, args=(address,))
        t.daemon = True  # daemon = True ends threads if main program closes
        t.start()
        threads.append(t)

    # Block main thread execution until all tasks in queue are done
    q.join()
    # Ensure all threads have finished final worker loops
    for t in threads:
        t.join()
    print()

    openPorts.sort()  # Sort list of discovered ports for readability
    for p in openPorts:
        print(f'[+] Port {p} is OPEN.')
    print('\nScanning complete.\n\n')


if __name__ == '__main__':
    main()
