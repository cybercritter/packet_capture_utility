"""
This class handles capturing the packets from the IP self.stack.
Packets captured will be only IP packets
"""
import pyshark
import time
from utilities.my_stack import CustomStack


class CustomPcap():
    def __init__(self, iface, timeout=10):
        self.buffer = []
        self.iface = iface
        self.timeout = timeout
        self.capture = pyshark.LiveCapture(
            interface=iface)
        self.stack = CustomStack()
        self.start_time = time.time()

    @property
    def empty(self):
        """
        The empty function checks if the stack is empty.
            :return: True if the stack is empty, False otherwise.

        :param self: Represent the instance of the class
        :return: True if the stack is empty and false otherwise
        """
        return self.stack.isempty(self.buffer)

    def get_packet_details(self, packet):
        """
        The get_packet_details function is designed to parse specific
        details from an individual packet.

        :param self: Represent the instance of the object itself
        :param packet: Get the raw packet from either a pcap file or via
                       live capture using tshark
        :return: A string containing the packet:
                 timestamp,
                 protocol
                 type,
                 source address,
                 source port,
                 destination address
                 destination port
        """
        protocol = packet.transport_layer
        if hasattr(packet, 'ip'):
            source_address = packet.ip.src
            source_port = packet[packet.transport_layer].srcport
            destination_address = packet.ip.dst
            destination_port = packet[packet.transport_layer].dstport
            packet_time = packet.sniff_time
            return f'Packet Timestamp: {packet_time}' \
                f'\nProtocol type: {protocol}' \
                f'\nSource address: {source_address}' \
                f'\nSource port: {source_port}' \
                f'\nDestination address: {destination_address}' \
                f'\nDestination port: {destination_port}\n'

    def _add_packet_to_buffer(self, packet):
        """
        The _add_packet_to_buffer function adds a packet to the buffer.

        :param self: Represent the instance of the class
        :param packet: Add a packet to the buffer
        :return: The packet that was added to the buffer
        """
        self.stack.push(stk=self.buffer, item=packet)

    def get_packet(self):
        """
        The pop_packet function is used to remove the first packet
        from the buffer.

        The function returns a tuple of (packet, port) where
        packet is a string and port is an integer.

        :param self: Represent the instance of the class
        :return: The packet at the head of the queue
        """
        try:
            if not self.stack.isempty(self.buffer):
                return self.stack.pop(self.buffer)
        except TypeError as e:
            print(e)

    def start_capture(self):
        """
        The start_capture function is the main function of this class.
        It captures packets from a socket and adds them to the buffer.)

        :param self: Refer to the object itself
        :return: A generator object
        """
        try:
            print(f"Capturing packets for {self.timeout} seconds")
            self.capture.sniff(timeout=30)

            for packet in self.capture._packets:
                self._add_packet_to_buffer(packet)
        except packet.StopCapture as e:
            print(e)
        self.capture.close()

        print()
