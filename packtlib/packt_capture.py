"""
This class handles capturing the packets from the IP stack.
Packets captured will be only IP packets
"""

import socket
from stack import Stack


class CustomPcap():
    def __init__(self):
        self.buffer = Stack(50)
        self.socket = None

    def create_socket(self):
        """
        The create_socket function creates a socket object.
        The function takes one argument, cls, which is the class
        that the function belongs to.
        The socket object is created using the AF_INET (IPv4),
        SOCK_RAW (raw sockets), and IPPROTO_TCP (TCP) parameters.

        :param cls: Pass the class to the function
        :return: A socket object
        """
        try:
            self.socket = socket.socket(
                socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        except socket.error as error:
            print(f'{error}')
            sys.exit()

    def _add_packet_to_buffer(self, packet):
        """
        The _add_packet_to_buffer function adds a packet to the buffer.

        :param self: Represent the instance of the class
        :param packet: Add a packet to the buffer
        :return: The packet that was added to the buffer
        """
        self.buffer.put(packet)

    def pop_packet(self):
        """
        The pop_packet function is used to remove the first packet
        from the buffer.

        The function returns a tuple of (packet, port) where
        packet is a string and port is an integer.

        :param self: Represent the instance of the class
        :return: The packet at the head of the queue
        """
        return self.buffer.get()

    def capture(self):
        """
        The capture function is the main function of this class.
        It captures packets from a socket and adds them to the buffer.)
        """
        try:
            packet_s = self.socket.recvfrom(65535)
            print(f'packet: {packet_s}')
        except socket.error as error:
            print(f'{error}')
        # self._add_packet_to_buffer(packet_s)


if __name__ == '__main__':
    import tty
    import sys
    import termios

    KEYPRESSED = 0
    PACKET = None
    pcap_test = CustomPcap()
    pcap_test.create_socket()

    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)

    print('begin')
    while KEYPRESSED != chr(ord('q'.lower())):  # Q
        KEYPRESSED = sys.stdin.read(1)[0]
        print("You pressed", KEYPRESSED)

        if KEYPRESSED == 'q':
            print(f'exiting {__name__}')
            sys.exit()

        pcap_test.capture()
        print('continue')

    print('end')
    # print(f'{pcap_test.pop_packet()}')

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
