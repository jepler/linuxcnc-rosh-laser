#!/usr/bin/python

import itertools
import PIL.Image as Image
import sys

FEED_LO = 450
FEED_HI = 1200

def rasterize_col(pixels, x, y0, dy):
    st = 0
    print "G0X%.2f" % x
    for a, b in itertools.groupby(pixels):
        b = len(list(b))
        if a != '\xff':
            print "M67E0Q0G1Y%.2f" % (y0 + st * dy)
            st += b
            o = FEED_LO + (FEED_HI - FEED_LO) * (ord(a)/255.)
            print "M67E0Q100F%fG1Y%.2f" % (o, y0 + st * dy)
        else:
            st += b
    print "M67E0Q0Z0"

STEPSIZE = 3/160.
TRAVEL = 36


i = Image.open(sys.argv[1])
i = i.convert("L")  # Force to B&W
w, h = i.size
dx = 4*STEPSIZE
dy = -dx
x0 = (TRAVEL-dx*w)/2
y0 = TRAVEL + (dy*h-TRAVEL)/2
x1 = x0 + w * dx
y1 = y0 - h * dy
def tobytes(i):
    if hasattr(i, 'tobytes'): return i.tobytes()
    return i.tostring()
data = tobytes(i)

print >>sys.stderr, len(data), w, h, w*h
print "G21"
print "M5"
print "M68 E0 Q0"
print "G64 P.1 Q.1"
print "F450"
#print "G0 X0 Y0"
#print "G0 X%f" % TRAVEL
#print "G0 Y%f" % TRAVEL
#print "G0 X0"
#print "G0 Y0"
#print "F%d" % FEED
print "M3S1"
for col in range(w):
    coldata = data[col : : w]
    #print >>sys.stderr, col, len(coldata)
    print "(%d)" % col
    x = x0 + dx * col
    if col % 2: rasterize_col(coldata[::-1], x, y0, -dy)
    else:       rasterize_col(coldata,       x, y1,  dy)
    print
#    if col % 100 == 99:
#        print "M68 E0 Q0"
#        print "G4 P60"
print "M2"

#    Convert greyscale images to gcode for laser engraving
#    Copyright 2015  Jeff Epler <jepler@unpythonic.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
