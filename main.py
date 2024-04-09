import pyshark
import time
import json

TIMEOUT = 15
start = time.time()
# Capture packets on the 'en0' interface
capture = pyshark.LiveCapture(interface='en0')

# Loop to continuously capture and process packets
for packet in capture.sniff_continuously():
    print(f'Packet length: {len(packet)}')
    print(f"Protocol: {packet.transport_layer}")
    print(f"Ethernet Header: {packet['eth'].src}")
    json.dump(packet, open("my.json", "w"))

    if time.time() - start > TIMEOUT:
        break

capture.clear()
capture.close()
