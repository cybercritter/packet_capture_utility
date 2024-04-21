"""
This class handles capturing the packets from the IP self.stack.
Packets captured will be only IP packets
"""
import pyshark
import time


class Capture:
    """
    A class for custom packet capture and analysis.

    Attributes:
        iface (str): The interface to capture packets from.
        timeout (int): The timeout value for packet capture (default is 10 seconds).
        buffer (list): A list to store captured packets.
        start_time (float): The start time of the capture process.

    Methods:
        empty (property): Check if the buffer stack is empty.
        get_packet_details(packet): Get details of a packet.
        _add_packet_to_buffer(packet): Add a packet to the buffer stack.
        get_packet(): Remove and return the first packet from the buffer.
        start_capture(): Start capturing packets and adding them to the buffer.
    """

    def __init__(self, iface, packet_count, timeout=10):
        """
        Initialize a CustomPcap object.

        Args:
            iface (str): The interface to capture packets from.
            timeout (int, optional): The timeout value for packet capture (default is 10 seconds).
        """
        self.packet_summary = {}
        self.iface = iface
        self.timeout = 30
        self.packet_count = packet_count
        self.start_time = time.time()

    def add_packet_to_buffer(self, packet):
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

        self.packet_summary.update({'packet_time': packet.sniff_time})
        self.packet_summary.update({'protocol': protocol})
        #
        if hasattr(packet, "ip"):
            self.packet_summary.update({'source_address': packet.ip.src})
            self.packet_summary.update({'source_port': packet[packet.transport_layer].srcport})
            self.packet_summary.update({'destination_address': packet.ip.dst})
            self.packet_summary.update({'destination_port': packet[packet.transport_layer].dstport})
            self.packet_summary.update({'packet_time': packet.sniff_time})

    @property
    def empty(self):
        """
        Check if the buffer is empty.

        Returns:
            bool: True if the buffer stack is empty, False otherwise.
        """
        if len(self.packet_summary) == 0:
            return True
        else:
            return False

    def get_packets(self):
            print(self.packet_summary)

    def get_packet(self):
        """
        Remove and return the first packet from the buffer.

        Returns:
            tuple: A tuple containing the packet and port number.
        """
        try:
            if not self.empty:
                print(self.packet_summary.pop('packet_time'), self.packet_summary.pop('protocol'))
        except TypeError as e:
            print(e)

    def start_capture(self):
        """
        Start capturing packets and adding them to the buffer.
        """
        # while True:
        #     if self.start_time + self.timeout < time.time():
        #         break
        #
        #     # Create a LiveCapture object, using the default interface
        #     capture = pyshark.LiveCapture(interface="en0")
        #
        #     # Start capturing packets
        #     # capture.sniff(packet_count=100)  # Capture packets for 10 seconds, for example
        #
        #     # Start capturing packets and apply the callback function to each packet
        #     capture.apply_on_packets(get_packet_details)

        #     # Create a LiveCapture object, using the default interface
        capture = pyshark.LiveCapture(interface="en0")

        for packet in capture.sniff_continuously(packet_count=10):
            # Print information about each captured packet
            self.add_packet_to_buffer(packet)

            # Check if the timeout has been reached
            if time.time() - self.start_time >= self.timeout:
                break
