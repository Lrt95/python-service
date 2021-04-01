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
    #packet = socket.inet_pton(socket.AF_INET, host)
    print(socket.getaddrinfo("127.0.0.1", 1025))
    # UDP
    socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    socket_udp.connect("", 0)
    ifname= "enp0s8"
   # info = fcntl.ioctl(socket_udp.fileno(), 0x8927, struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    # TCP
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp.connect(("localhost", 1029))

    while True:
        packet = socket_udp.recvfrom(2048)
        print(packet[0][:14])
    # not idea
    # print(socket.if_nameindex())


def main():
    snifer()


if __name__ == '__main__':
    main()
