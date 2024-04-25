![Pylint](https://github.com/cybercritter/packet_capture_utility/actions/workflows/pylint.yml/badge.svg)

# Author and class information
```
Author: Michael Reid
Final Project: CS 1400 (Spring 2024)
Instructor: John Adamic
```

# Packet Capture utility
Capture packets from the IP stack
---
Capture packets from a specified network interface and write packet summary for ip layer packets to a JSON file.<br>

The packet header information  will be used to store summary in user readable format.
****

## Python dependencies
All module dependencies are in the requirements.txt file.<br>
Use the Python command pip to install the dependencies. <i>pip install -r requirements.txt</br>

# Other dependencies
This program needs the tshark library. The easiest way to acquire it is to install Wireshark<br>
which can be downloaded from the Wireshark website https://www.wireshark.org/download.html</br>

This app uses the 4.2.4 version. However, it is expected to support later versions.
***
## OS's Tested
This program has been tested on Windows 10 and MacOS Sonoma.

Linux should be supported but is untested
***

## Help and examples of use
```bash
PS C:\Users\cyber\Documents\projects\packet_capture_utility> python .\capture_packets.py -h
usage: capture_packets.py [-h] -i INTERFACE [-t TIMEOUT] [-o OUTPUT]

Capture packets from a specified network interface and write packet summary for ip layer packets to a JSON file.

options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Network interface name (e.g., eth0)
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout duration in seconds default 10 seconds
  -o OUTPUT, --output OUTPUT
                        Output JSON file path: default is ./packets.json

Examples:
Mac/Linux
$ python capture_packets.py -i en0 -t 10 -o captured_packets.json

Windows
$ python capture_packets.py -i Ethernet -t 10 -o captured_packets.json
```

