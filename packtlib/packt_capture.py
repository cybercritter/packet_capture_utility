"""
This class handles capturing the packets from the IP self.stack.
Packets captured will be only IP packets
"""
import pyshark
import time
from datetime import datetime


class Capture:
    def __init__(self, iface, timeout=10):
        self.packet_summary = []
        self.iface = iface
        self.timeout = timeout
        self.capture = None
        self.start_time = time.time()

    @staticmethod
    def add_packet_to_buffer(packet):

        try:
            if hasattr(packet, "ip"):
                return {
                    "timestamp": packet.sniff_time.timestamp(),
                    "protocol": packet.highest_layer,
                    "source": packet.ip.src,
                    "destination": packet.ip.dst,
                    "length": packet.length
                }
        except TypeError:
            return None

    @property
    def is_empty(self):
        if len(self.packet_summary) == 0:
            return True
        else:
            return False

    @property
    def packet_num_packet_captured(self):
        return len(self.packet_summary)

    def start_capture(self):
        time2 = time.localtime().tm_sec
        self.capture = pyshark.LiveCapture(interface="en0")

        self.capture = pyshark.LiveCapture(interface=self.iface)

        for packet in self.capture.sniff_continuously():
            # when a packet is captured
            self.packet_summary.append(self.add_packet_to_buffer(packet))
            time1 = int(time.localtime().tm_sec)
            time_elapsed = time1 - time2
            if time_elapsed == 1:
                print(f"#", end='')
            # Check if the timeout has been reached
            if time.time() - self.start_time >= self.timeout:
                print()
                break
            time2 = int(time.localtime().tm_sec)
