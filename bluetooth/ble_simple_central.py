#!/usr/bin/env python3

from __future__ import print_function
from gattlib import DiscoveryService
 
class DiscoverDevice():
    def GetDeviceList(self):
        service = DiscoveryService("hci0")
        device = service.discover(2)
        return device
 
if __name__ == '__main__':
    devList = DiscoverDevice().GetDeviceList()
    for address, name in devList.items():
        print("name: {}, address: {}".format(name, address))