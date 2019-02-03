from socket import *

import struct

import sys

import time


NTP_SERVER = 'eg.pool.ntp.org'  # NTP server domain that i wish to send requests to 

TIME1970 = 2208988800      # 1970-01-01 00:00:00


def sntp_client():

    client = socket(AF_INET, SOCK_DGRAM)  #displays the socket object 

    # default sending message
    data = bytes('\x1b' + 47 * '\0', encoding="utf8")

    client.sendto(data, (NTP_SERVER, 123))  # sending  UDP packet

    data, address = client.recvfrom(1024)   # this code records the  response from the  server

    if data:

        print('Response received from:', address)  # prints server address

        t = struct.unpack('!12I', data)[10]  # extract  the timestamp

        t -= TIME1970  # calculates the time using the 1970 format 

        print('\tTime=%s' % time.ctime(t))


if __name__ == '__main__':

    sntp_client()
