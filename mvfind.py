#!/usr/bin/python


import sys


db_name = "mlist/db"

class MAC:

    def __init__(self, mac, vendor="Unknown"):
        self.mac = mac
        self.vendor = vendor

    def __str__(self):
        return "{}\t{}".format(self.mac, self.vendor)


def read_mac_to_find(file_name):
    mac_list = []
    try:
        file = open(file_name, 'r')
        for line in file:
            mac_list.append(MAC(line.strip()))
    except OSError as msg:
        print(msg)
    return mac_list


def find_mac_vendor(mac_list):
    s_list = list(mac_list)

    try:
        with open(db_name, 'r') as f:
            for line in f:
                if len(s_list) > 0:
                    for m in s_list:
                        key = m.mac[:8]
                        if key in line:
                            m.vendor = line.split('\t')[1].strip()
                            s_list.remove(m)
                else:
                    break

    except OSError as msg:
        print(msg)


def print_usage():
    print("MAC address vendor finder\n"
          "Usage:\n"
          "\tmvfind [MAC Address]...\n"
          "\tmvfind -f ./file_name\n"
          "where -f is path to file containing list of MAC address to find.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    mac_list = []

    if sys.argv[1] == '-f':
        if len(sys.argv) < 3:
            print_usage()
            sys.exit(1)
        else:
            mac_list = read_mac_to_find(sys.argv[2])
    else:
        for m in sys.argv[1:]:
            mac_list.append(MAC(m))

    find_mac_vendor(mac_list)

    print("{:17}\t{}".format('[MAC Address]', '[Vendor]'))
    for m in mac_list:
        print(m)
