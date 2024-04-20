
def get_packet_details(packet):
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
    packet_summary = {}
    packet_summary.update({'packet_time': packet.packet_time})
    packet_summary.update({'protocol': protocol})

    if hasattr(packet, "ip"):
        packet_summary.update({'source_address': packet.ip.src})
        packet_summary.update({'source_port': packet[packet.transport_layer].srcport})
        packet_summary.update({'destination_address': packet.ip.dst})
        packet_summary.update({'destination_port': packet[packet.transport_layer].dstport})
        packet_summary.update({'packet_time': packet.sniff_time})

        return packet_summary
