"""Module sniffer

"""

import socket
import json
import struct
import fcntl
import binascii


def snifer():
    # AF_PACKET if for Linux
    # AF_INET if for socket
    # rawSocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    host = socket.gethostbyname(socket.gethostname())
    print(host)
    # packet = socket.inet_pton(socket.AF_INET, host)
   # print(socket.getaddrinfo("127.0.0.1", 1025))
    # UDP

    # info = fcntl.ioctl(socket_udp.fileno(), 0x8927, struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    # TCP
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    socket_tcp.bind((host, 0))
    socket_tcp.connect(("", 0))
    socket_tcp.listen()

   # data = socket_tcp.getpacket()
  #  print(data)
   # socket_tcp.connect(("localhost", 1029))
    print(socket_tcp.accept())

    while True:
        packet = socket_tcp.recvfrom(2048)
        print(packet)


if __name__ == "__main__":
    snifer()
#
#
# # def main():
# #   snifer()
#
#
# import socket
# import struct
# import binascii
# import textwrap
# import fcntl
#
# # def main():
# # Get host
# host = socket.gethostbyname(socket.gethostname())
# print('IP: {}'.format(host))
#
# # Create a raw socket and bind it
# conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
# conn.bind((host, 0))
#
# # Include IP headers
# conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
# # Enable promiscuous mode
# fcntl.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
#
# while True:
#     # Recive data
#     raw_data, addr = conn.recvfrom(65536)
#
#     # Unpack data
#     dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
#
#     print('\nEthernet Frame:')
#     print("Destination MAC: {}".format(dest_mac))
#     print("Source MAC: {}".format(src_mac))
#     print("Protocol: {}".format(eth_proto))
#
#
# # Unpack ethernet frame
# def ethernet_frame(data):
#     dest_mac, src_mac, proto = struct.unpack('!6s6s2s', data[:14])
#     return get_mac_addr(dest_mac), get_mac_addr(src_mac), get_protocol(proto), data[14:]
#
#
# # Return formatted MAC address AA:BB:CC:DD:EE:FF
# def get_mac_addr(bytes_addr):
#     bytes_str = map('{:02x}'.format, bytes_addr)
#     mac_address = ':'.join(bytes_str).upper()
#     return mac_address
#
#
# # Return formatted protocol ABCD
# def get_protocol(bytes_proto):
#     bytes_str = map('{:02x}'.format, bytes_proto)
#     protocol = ''.join(bytes_str).upper()
#     return protocol

#
# import fcntl
# import socket
# import struct
# import binascii
#
#
# def get_hw_address(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', bytes(ifname[:15], 'utf-8')))
#     return ''.join(l + ':' * (n % 2 == 1) for n, l in enumerate(binascii.hexlify(info[18:24]).decode('utf-8')))[:-1]
#
#
# import psutil
# def test():
#     addrs = psutil.net_if_addrs()
#     print(addrs.keys())
#
#
# from ctypes import *
#
# class Sockaddr(Structure):
#     _fields_ = [('sa_family', c_ushort), ('sa_data', c_char * 14)]
#
# class Ifa_Ifu(Union):
#     _fields_ = [('ifu_broadaddr', POINTER(Sockaddr)),
#                 ('ifu_dstaddr', POINTER(Sockaddr))]
#
# class Ifaddrs(Structure):
#     pass
#
# Ifaddrs._fields_ = [('ifa_next', POINTER(Ifaddrs)), ('ifa_name', c_char_p),
#                     ('ifa_flags', c_uint), ('ifa_addr', POINTER(Sockaddr)),
#                     ('ifa_netmask', POINTER(Sockaddr)), ('ifa_ifu', Ifa_Ifu),
#                     ('ifa_data', c_void_p)]
#
#
# def get_interfaces():
#     libc = CDLL('libc.so.6')
#     libc.getifaddrs.restype = c_int
#     ifaddr_p = pointer(Ifaddrs())
#     ret = libc.getifaddrs(pointer((ifaddr_p)))
#     interfaces = set()
#     head = ifaddr_p
#     while ifaddr_p:
#         interfaces.add(ifaddr_p.contents.ifa_name)
#         ifaddr_p = ifaddr_p.contents.ifa_next
#     libc.freeifaddrs(head)
#     return interfaces
#
# import os
# def getAllInterfaces():
#     return os.listdir('/sys/class/net/')


from get_nic import getnic


def test():
    getnic.interfaces()

    interfaces = getnic.interfaces()
    getnic.ipaddr(interfaces)
    print(interfaces)

# test()
# print(getAllInterfaces())
# if __name__ == '__main__':
# # get_hw_address("enp0s8")
#     test()
