"""
This class handles capturing the packets from the IP self.stack.
Packets captured will be only IP packets
"""
import pyshark
import time
from utilities.my_stack import CustomStack


class CustomPcap:
    """
    A class for custom packet capture and analysis.

    Attributes:
        iface (str): The interface to capture packets from.
        timeout (int): The timeout value for packet capture (default is 10 seconds).
        buffer (list): A list to store captured packets.
        stack (CustomStack): An instance of CustomStack for managing the buffer.
        start_time (float): The start time of the capture process.

    Methods:
        empty (property): Check if the buffer stack is empty.
        get_packet_details(packet): Get details of a packet.
        _add_packet_to_buffer(packet): Add a packet to the buffer stack.
        get_packet(): Remove and return the first packet from the buffer.
        start_capture(): Start capturing packets and adding them to the buffer.
    """

    def __init__(self, iface, timeout=10):
        """
        Initialize a CustomPcap object.

        Args:
            iface (str): The interface to capture packets from.
            timeout (int, optional): The timeout value for packet capture (default is 10 seconds).
        """
        self.buffer = []
        self.iface = iface
        self.timeout = timeout
        self.capture = pyshark.LiveCapture(interface=iface)
        self.stack = CustomStack()
        self.start_time = time.time()

    @property
    def empty(self):
        """
        Check if the buffer stack is empty.

        Returns:
            bool: True if the buffer stack is empty, False otherwise.
        """
        return self.stack.isempty(self.buffer)

    def get_packet_details(self, packet):
        """
        Get details of a packet, including protocol type,
        source and destination addresses,
        source and destination ports, and packet timestamp.

        Args:
            packet: The packet for which to retrieve details.

        Returns:
            str: A formatted string containing the packet details.
        """
        protocol = packet.transport_layer
        if hasattr(packet, "ip"):
            source_address = packet.ip.src
            source_port = packet[packet.transport_layer].srcport
            destination_address = packet.ip.dst
            destination_port = packet[packet.transport_layer].dstport
            packet_time = packet.sniff_time
            return (
                f"Packet Timestamp: {packet_time}"
                f"\nProtocol type: {protocol}"
                f"\nSource address: {source_address}"
                f"\nSource port: {source_port}"
                f"\nDestination address: {destination_address}"
                f"\nDestination port: {destination_port}\n"
            )

    def _add_packet_to_buffer(self, packet) -> None:
        """
        Adds a packet to the buffer stack.

        Args:
            packet: The packet to add to the buffer stack.

        Returns:
            None
        """
        self.stack.push(stk=self.buffer, item=packet)

    def get_packet(self):
        """
        Remove and return the first packet from the buffer.

        Returns:
            tuple: A tuple containing the packet and port number.
        """
        try:
            if not self.stack.isempty(self.buffer):
                return self.stack.pop(self.buffer)
        except TypeError as e:
            print(e)

    def start_capture(self):
        """
        Start capturing packets and adding them to the buffer.
        """
        try:
            print(f"Capturing packets for {self.timeout} seconds")
            self.capture.sniff(timeout=30)

            for packet in self.capture._packets:
                self._add_packet_to_buffer(packet)
        except packet.StopCapture as e:
            print(e)
        self.capture.close()
