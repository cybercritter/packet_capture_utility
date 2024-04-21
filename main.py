"""
A simple script to demonstrate packet capture using CustomPcap class.

Usage:
    Run this script to capture packets from the specified interface
    and print the number of packets captured.

Example:
    $ python capture_script.py
"""

from packtlib.packt_capture import Capture

if __name__ == '__main__':
    # Initialize CustomPcap object for capturing packets from interface
    # 'en0' with a timeout of 30 seconds
    pcap_test = Capture('en0', timeout=10, packet_count=1000)
    print(f'Starting Capture on interface: {pcap_test.iface}')
    pcap_test.start_capture()

    print('End Capture')

    # Print the number of packets captured
    buffers = pcap_test.get_packet()

    try:
        print(f'Number of packets captured: {len(buffers)}')
    except Exception as e:
        print(f'Error: {e}')

    # packet = pcap_test.get_packet()
    # print(packet)
    # Uncomment the following block to print details of each captured packet
    # for packet in pcap_test.buffer:
    #     try:
    #         print(pcap_test.get_packet_details(packet))
    #     except AttributeError:
    #         '''
    #         if Attribute type is not in the attribute list, just ignore
    #         the packet
    #         '''
