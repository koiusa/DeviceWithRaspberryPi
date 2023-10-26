#!/usr/bin/env python3

import asyncio
from bleak import BleakScanner

async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"{d} : [{d.rssi}: {d.metadata}]")

asyncio.run(run())