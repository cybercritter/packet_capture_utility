import ctypes, sys
from ctypes.util import find_library

if sys.platform == "darwin":
    _pcap = ctypes.cdll.LoadLibrary(find_library("libpcap"))
elif sys.platform == "linux2":
    _pcap = ctypes.cdll.LoadLibrary("libpcap.so")

errbuf = ctypes.create_string_buffer(256)
pcap_close = _pcap.pcap_close

pcap_lookupdev = _pcap.pcap_lookupdev
pcap_lookupdev.restype = ctypes.c_char_p
dev = pcap_lookupdev(errbuf)
print(f"Attching to {dev}")

pcap_create = _pcap.pcap_create
pcap_create.restype = ctypes.c_void_p
handle = pcap_create(dev, errbuf)

if not handle:
    print("failed creating handler:",errbuf)
    exit()

pcap_activate = _pcap.pcap_activate
pcap_activate.argtype = [ctypes.c_void_p]

errbuf = pcap_activate(handle)
print(errbuf)

# monitor mode
pcap_can_set_rfmon = _pcap.pcap_can_set_rfmon
pcap_can_set_rfmon.argtypes = [ctypes.c_void_p]
print("can rfmon:",pcap_can_set_rfmon(handle))

