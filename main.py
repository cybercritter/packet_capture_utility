"""main.py"""
from packtlib.packt_capture import CustomPcap

if __name__ == '__main__':

    pcap_test = CustomPcap('en0', timeout=30)
    print(f'Starting Capture on interface: {pcap_test.iface}')
    pcap_test.start_capture()
    print('End Capture')

    print(f'Number of packets captured: {len(pcap_test.buffer)}')

    # for packet in pcap_test.buffer:
    #     try:
    #         print(pcap_test.get_packet_details(packet))
    #     except AttributeError:
    #         '''
    #         if Attribute type is not in the attribute list, just ignore
    #         the packet
    #         '''
