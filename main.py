"""
A simple script to demonstrate packet capture using CustomPcap class.

Usage:
    Run this script to capture packets from the specified interface
    and print the number of packets captured.

Example:
    $ python capture_script.py
"""

from packtlib.packt_capture import Capture
import json

if __name__ == '__main__':
    # Initialize CustomPcap object for capturing packets from interface
    # 'en0' with a timeout of 30 seconds
    pcap_test = Capture('en0', timeout=10)
    print(f'Starting Capture on interface: {pcap_test.iface}')
    pcap_test.start_capture()

    print('End Capture')

    try:
        print(f'Number of packets captured: {pcap_test.packet_num_packet_captured}')
    except Exception as e:
        print(f'Error: {e}')

    # for packet in pcap_test.packet_summary:
    #     try:
    #         if packet is not None:
    #             print(packet)
    #     except AttributeError:
    #         '''
    #         if Attribute type is not in the attribute list, just ignore
    #         the packet
    #         '''
    with open('pcap_files/packets.json', 'w+') as outfile:
        json.dump(pcap_test.packet_summary, outfile, indent=2)

