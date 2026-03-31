# Port-Scanner-Demo

A technical demonstration of concurrent networking and network socket handling in Python.

## Description

This project is a CLI-based TCP port scanner designed to teach myself how to implement TCP connections and safely synchronize multiple threads in Python. By distributing connection attempts across a pool of 50 or more worker threads, the scanner evaluates large port ranges concurrently, bypassing the latency of sequential scans.

## Getting Started

### Dependencies

* Python 3.6+: The script utilizes f-strings and the argparse library.
* OS: Cross-platform (Windows, macOS, Linux).
* Network: Requires permissions to initiate outgoing TCP connections

### Installing

* Clone the repository to your local machine:
```
git clone https://github.com/adamchapdelaine/Port-Scanner-Demo.git
```
* Navigate into the project directory:
```
cd Port-Scanner-Demo
```

### Executing program

* Run the scanner against a target IP or hostname (default scan is ports 1-1000):
```
python scanner.py 192.168.1.1
```
* To scan a specific range:
```
python scanner.py 192.168.1.1 --ports 20-443
```
* To scan a single port:
```
python scanner.py 192.168.1.1 --ports 80
```
* Expected output:
```
Scanning 192.168.1.1...
........................
[+] Port 80 is OPEN.
[+] Port 443 is OPEN.

Scanning complete.
```

## Help

* Timeouts: If you are on a high-latency network, you may need to increase the TIMEOUT constant in the source code to ensure accurate results.
* Permission Denied: Some restricted environments or firewalls may block rapid outgoing connection attempts. Ensure you have the right to scan the target IP.
* To view all available arguments and their default values, run: 
```
python scanner.py --help
```

## Authors

Adam Chapdelaine
* GitHub: @adamchapdelaine
* Professional Handle: chapdela

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

* ISC2 Certified in Cybersecurity (CC) Curriculum: For providing the foundational knowledge on port-based vulnerabilities.
* PortSwigger Academy: For inspiration regarding server-side vulnerability research.
* [DomPizzie](https://gist.github.com/DomPizzie) for the README template.
