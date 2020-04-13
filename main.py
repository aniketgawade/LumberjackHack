#!/usr/bin/python
import struct
import operator
import Quartz.CoreGraphics as CG
import time
import sys, getopt
from pynput.keyboard import Key, Controller

def main():
    args = getopt.getopt(sys.argv[1:], '')
    keyboard = Controller()

    argx = args[1][0]
    argy = args[1][1]
    global x
    x = int(argx)
    global y
    y = int(argy)

    sp = ScreenPixel()
    while True:
        sp.capture()
        r,g,b = sp.pixel(0, 0)
        if r == 212 and g == 247 and b == 254:
            print sp.pixel(0,0)
            keyboard.press(Key.right)
            time.sleep(0.15)
            keyboard.release(Key.right)
        else:
            print sp.pixel(0,0)
            keyboard.press(Key.left)
            time.sleep(0.15)
            keyboard.release(Key.left)
              

class ScreenPixel(object): 
    def capture(self):
        region = CG.CGRectMake(x, y, 1, 1)
 
        # Create screenshot as CGImage
        image = CG.CGWindowListCreateImage(
            region,
            CG.kCGWindowListOptionOnScreenOnly,
            CG.kCGNullWindowID,
            CG.kCGWindowImageDefault)
 
        # Intermediate step, get pixel data as CGDataProvider
        prov = CG.CGImageGetDataProvider(image)
 
        # Copy data out of CGDataProvider, becomes string of bytes
        self._data = CG.CGDataProviderCopyData(prov)
 
        # Get width/height of image
        self.width = CG.CGImageGetWidth(image)
        self.height = CG.CGImageGetHeight(image)
 
    def pixel(self, x, y):
        # Pixel data is unsigned char (8bit unsigned integer),
        # and there are four (blue,green,red,alpha)
        data_format = "BBBB"
 
        # Unpack data from string into Python'y integers
        b, g, r, a = struct.unpack_from(data_format, self._data, offset=0)
        
        # Return BGRA as RGBA
        return (r, g, b) 
 
if __name__ == '__main__':
    main()
