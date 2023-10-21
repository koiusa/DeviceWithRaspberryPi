#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
 
from pyPS4Controller.controller import Controller
import sys
 
args = sys.argv
 
if(len(args) < 2):
    js_num = str(0)
else:
    js_num = args[1]
 
 
class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    # Implementation if any input is received.
    # Example
    # ---
    def on_circle_press(self):
        super().on_circle_press()

    def on_R2_press(self,value):
        super().on_R2_press(value)
    # ---
 
controller = MyController(interface="/dev/input/js" + js_num, connecting_using_ds4drv=False)
controller.listen()
