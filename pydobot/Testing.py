import time
from glob import glob

from dobot import *

# Connecting to dobot
available_ports = glob('/dev/cu*usb*')  # mask for OSX Dobot port
if len(available_ports) == 0:
    print('no port found for Dobot Magician')
    exit(1)

device = Dobot(port=available_ports[0])
x = 0
y = 0

zeta = input(">>>")
if zeta == "":
    '''
    x1 = 0
    y1 = 7.5
    
    device.jump(205, 12.5, 0)
    time.sleep(1)
    device.go(205, 12.5, -35)
    while (x <= 212.5):
        x1 += 0.75
        y1 = (56.25-(x)**2)**0.5
        x = x1+ 205
        y = y1 + 5
        print(x,y,y1,x1)
        device.go(x, y, -35)

    '''

    device.jump(205, 12.5, -35)
    device.go(205, 12.5+2.5, -35)
    device.go(205+5.303, 12.5+2.5+5.303, -35)
    device.go(205+5.303+5, 12.5+2.5+5.303, -35)
    device.go(205+5.303+5+5.303, 12.5+2.5, -35)
    device.go(205+5.303+5+5.303, 12.5-2.5, -35)
    device.go(205+5.303+5, 12.5-2.5-5.303, -35)
    device.go(205+5.303, 12.5-2.5-5.303, -35)
    device.go(205, 12.5-2.5, -35)
    device.go(205, 12.5+1, -35)
