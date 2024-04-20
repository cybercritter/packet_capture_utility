"""
This class handles capturing the packets from the IP self.stack.
Packets captured will be only IP packets
"""
import pyshark
import time
from utilities.customstack import CustomStack


class Capture(CustomStack):
    """
    A class for custom packet capture and analysis.

    Attributes:
        iface (str): The interface to capture packets from.
        timeout (int): The timeout value for packet capture (default is 10 seconds).
        stack (list): A list to store captured packets.
        stack (CustomStack): An instance of CustomStack for managing the buffer.
        start_time (float): The start time of the capture process.

    Methods:
        empty (property): Check if the buffer stack is empty.
        get_packet_details(packet): Get details of a packet.
        _add_packet_to_buffer(packet): Add a packet to the buffer stack.
        get_packet(): Remove and return the first packet from the buffer.
        start_capture(): Start capturing packets and adding them to the buffer.
    """

    def __init__(self, iface, packet_count, timeout=10, stack=None):
        """
        Initialize a CustomPcap object.

        Args:
            iface (str): The interface to capture packets from.
            timeout (int, optional): The timeout value for packet capture (default is 10 seconds).
        """
        self.stack = stack
        self.iface = iface
        self.timeout = timeout
        self.packet_count = packet_count
        self.start_time = time.time()

    @property
    def empty(self):
        """
        Check if the buffer stack is empty.

        Returns:
            bool: True if the buffer stack is empty, False otherwise.
        """
        return self.stack.isempty()

    def _add_packet_to_buffer(self, packet) -> None:
        """
        Adds a packet to the buffer stack.

        Args:
            packet: The packet to add to the buffer stack.

        Returns:
            None
        """
        self.stack.push(item=packet)

    def get_packet(self):
        """
        Remove and return the first packet from the buffer.

        Returns:
            tuple: A tuple containing the packet and port number.
        """
        try:
            if not self.stack.isempty():
                return self.stack.pop()
        except TypeError as e:
            print(e)

    def start_capture(self):
        """
        Start capturing packets and adding them to the buffer.
        """
        count = 0
        capture = pyshark.LiveCapture(interface=self.iface)
        try:
            print(f"Capturing packets for {self.timeout} seconds")
            capture.sniff(packet_count=self.packet_count)
        except TypeError as e:
            print(e)

            capture.close()

            for packet in capture._packets:
                self._add_packet_to_buffer(packet)
                count += 1
                print(f"{count} packets captured", end="\r")

            if len(capture._packets) <= 0:
                raise
            return self.stack


