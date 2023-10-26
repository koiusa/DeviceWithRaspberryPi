#!/usr/bin/env python3

from __future__ import print_function
from gattlib import DiscoveryService

class DiscoverDevice():

    def GetDeviceList(self):
        self._service = DiscoveryService("hci0")
        self._device = self._service.discover(2)
        return self._device
    
    def Show(self):
        devList = self.GetDeviceList()
        for address, name in devList.items():
            print("name: {}, address: {}".format(name, address))
 
if __name__ == '__main__':
    device = DiscoverDevice()
    device.Show()