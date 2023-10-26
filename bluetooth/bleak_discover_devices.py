#!/usr/bin/env python3

import asyncio
from bleak import BleakScanner

async def run():
    devices = await BleakScanner.discover(return_adv=True)
    for key in devices:
        d,a = devices[key]
        print(f"{d} : {a}")

asyncio.run(run())