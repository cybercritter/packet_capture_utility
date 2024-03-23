<<<<<<< Updated upstream
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

||||||| Stash base
=======
"""
Packet capture utility
"""

import ctypes as ct
import sys
from ctypes.util import find_library

# load the pcap library
if sys.platform == "darwin":
    _pcap = ct.cdll.LoadLibrary(find_library("libpcap"))
elif sys.platform == "linux2":
    _pcap = ct.cdll.LoadLibrary("libpcap.so")


# pcap functions Documentation for functions can be found here
# https://www.tcpdump.org/manpages/pcap.3pcap.html


# pull in functions directly

# set the resource types here
(_pcap.pcap_lookupdev).restype = ct.c_char_p
(_pcap.pcap_create).restype = ct.c_void_p
(_pcap.pcap_set_promisc).restype = ct.c_int
(_pcap.pcap_findalldevs).restyoe = ct.c_int


pcap_create = _pcap.pcap_create
pcap_create.restype = ct.c_void_p

# pcap_can_set_rfmon = _pcap.pcap_can_set_rfmon
# pcap_can_set_rfmon.argtypes = [ct.c_void_p]

pcap_set_promisc = _pcap.pcap_set_promisc
pcap_set_promisc.argtypes = [ct.c_void_p, ct.c_int]

pcap_perror = _pcap.pcap_perror
_pcap.pcap_perror.argtypes = [ct.c_void_p, ct.c_char_p]

pcap_findalldevs = _pcap.pcap_findalldevs
_pcap.pcap_findalldevs .argtypes = [C.POINTER(ct.c_void_p), ct.c_char_p]


# create buffer to capture error messages
errbuf = ct.create_string_buffer(256)

# lookup active device
# dev = (_pcap.pcap_lookupdev)(errbuf)
# print(f'{dev}')
devs = [[]]
pcap_findalldevs(devs, errbuf)

# create a new pcap instance
handle = pcap_create(devs[0], errbuf)
if not handle:
    print("failed creating handler:", errbuf)
    exit()

# put the interface in monitor mode
errono = pcap_set_promisc(handle, 1)
if errono < 0:
    pcap_perror(handle, errbuf)
elif errono == 1:
    print(f"{dev} is in monitor mode")

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
