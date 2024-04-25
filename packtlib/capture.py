"""
This class handles capturing the packets from the IP self.stack.
Packets captured will be only IP packets
"""
import time

import pyshark


class Capture:
    """
    A class for capturing network packets using PyShark.

    Attributes:
        packet_summary (list): A list to store summary information of captured packets.
        iface (str): The name of the network interface to capture packets from.
        timeout (int): Timeout duration for capturing packets in seconds.
        capture: PyShark LiveCapture object for capturing packets.
        start_time (float): Timestamp when the capture started.

    Methods:
        add_packet_to_buffer(packet): Static method to add packet information to the summary buffer.
        is_empty: Property method to check if the packet summary is empty.
        packet_num_packet_captured: Property method to get the number of packets captured.
        start_capture(): Method to start capturing packets continuously until
                         the timeout is reached.
    """

    def __init__(self, iface, timeout=10):
        """
        Initializes a Capture instance.

        Args:
            iface (str): The name of the network interface
                         to capture packets from.
            timeout (int, optional): Timeout duration for capturing
                                    packets in seconds. Defaults to 10.
        """
        self.packet_summary = []
        self.iface = iface
        self.timeout = timeout
        self.capture = None
        self.start_time = time.time()

    @staticmethod
    def add_packet_to_buffer(packet):
        """
        Adds packet information to the summary buffer.

        Args:
            packet: PyShark packet object.

        Returns:
            dict or None: Dictionary containing packet information
                          if packet has IP layer, None otherwise.
        """
        try:
            if hasattr(packet, "ip"):
                return {
                    "timestamp": packet.sniff_time.timestamp(),
                    "protocol": packet.highest_layer,
                    "source": packet.ip.src,
                    "destination": packet.ip.dst,
                    "length": packet.length
                }

            return None
        except TypeError:
            return None

    @property
    def is_empty(self):
        """
        Checks if the packet summary is empty.

        Returns:
            bool: True if packet summary is empty, False otherwise.
        """
        return len(self.packet_summary) == 0

    @property
    def packet_num_packet_captured(self):
        """
        Gets the number of packets captured.

        Returns:
            int: Number of packets captured.
        """
        return len(self.packet_summary)

    def start_capture(self):
        """
        Starts capturing packets continuously until the timeout is reached.
        """
        time2 = time.localtime().tm_sec
        self.capture = pyshark.LiveCapture(interface=self.iface)

        for packet in self.capture.sniff_continuously():
            # when a packet is captured
            self.packet_summary.append(self.add_packet_to_buffer(packet))
            time1 = int(time.localtime().tm_sec)
            time_elapsed = time1 - time2
            if time_elapsed == 1:
                print("#", end='')
            # Check if the timeout has been reached
            if time.time() - self.start_time >= self.timeout:
                print()
                break
            time2 = int(time.localtime().tm_sec)


#
# class Capture:
#     def __init__(self, iface, timeout=10):
#         self.packet_summary = []
#         self.iface = iface
#         self.timeout = timeout
#         self.capture = None
#         self.start_time = time.time()
#
#     @staticmethod
#     def add_packet_to_buffer(packet):
#
#         try:
#             if hasattr(packet, "ip"):
#                 return {
#                     "timestamp": packet.sniff_time.timestamp(),
#                     "protocol": packet.highest_layer,
#                     "source": packet.ip.src,
#                     "destination": packet.ip.dst,
#                     "length": packet.length
#                 }
#         except TypeError:
#             return None
#
#     @property
#     def is_empty(self):
#         if len(self.packet_summary) == 0:
#             return True
#         else:
#             return False
#
#     @property
#     def packet_num_packet_captured(self):
#         return len(self.packet_summary)
#
#     def start_capture(self):
#         time2 = time.localtime().tm_sec
#         self.capture = pyshark.LiveCapture(interface="en0")
#
#         self.capture = pyshark.LiveCapture(interface=self.iface)
#
#         for packet in self.capture.sniff_continuously():
#             # when a packet is captured
#             self.packet_summary.append(self.add_packet_to_buffer(packet))
#             time1 = int(time.localtime().tm_sec)
#             time_elapsed = time1 - time2
#             if time_elapsed == 1:
#                 print(f"#", end='')
#             # Check if the timeout has been reached
#             if time.time() - self.start_time >= self.timeout:
#                 print()
#                 break
#             time2 = int(time.localtime().tm_sec)
