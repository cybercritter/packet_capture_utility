#!/bin/python3
"""
Capture packets from a specified network interface and write packet
summary to a JSON file.


This script initializes a Capture object from the packtlib module
to capture packets from the specified network interface with a
timeout. It then prints the number of captured packets and writes the
packet summary to a JSON file.

Requirements:
- packtlib module with Capture class

Usage:
1. Ensure the required modules are installed. The required modules are in a requirements.txt file
2. Run the script.
"""

import argparse
import json

# disabled this error as the program runs.
# pylint: disable=import-error
from packtlib.capture import Capture

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Capture packets from a  '
                                     'specified network'
                                     'interface and write packet summary '
                                     'for ip layer packets to a JSON file.',
                                     epilog='Examples:\n'
                                            'Mac/Linux\n'
                                            '$ python capture_packets.py -i '
                                            'en0 -t 10 -o '
                                            'captured_packets.json\n\n'
                                            'Windows\n'
                                            '$ python capture_packets.py '
                                            '-i Ethernet -t 10'
                                            '-o captured_packets.json\n',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--interface', type=str,
                        help='Network interface name (e.g., eth0)',
                        required=True)
    parser.add_argument('-t', '--timeout', type=int,
                        help='Timeout duration in seconds default 10 seconds',
                        default=10)
    parser.add_argument('-o', '--output', type=str,
                        help='Output JSON file path:'
                             'default is ./packets.json',
                        default='packets.json')

    args = parser.parse_args()

    # Initialize Capture object for capturing packets
    pcap_test = Capture(args.interface, timeout=args.timeout)

    # Start capturing packets
    print(f'Starting Capture on interface: {pcap_test.iface}')
    pcap_test.start_capture()
    print('End Capture')

    # Print the number of packets captured
    print('Number of packets captured: '
          f'{pcap_test.packet_num_packet_captured}')

    # Write packet summary to a JSON file
    with open(args.output, 'w+', encoding='utf-8') as outfile:
        json.dump(pcap_test.packet_summary, outfile, indent=2)
