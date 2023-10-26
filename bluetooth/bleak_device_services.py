#!/usr/bin/env python3

import sys
import asyncio
from bleak import BleakClient

address = sys.argv[1]

async def run(address):
    async with BleakClient(address) as client:
        for s in client.services:
            print(s)

asyncio.run(run(address))