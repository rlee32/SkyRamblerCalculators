#!/usr/bin/env python

import sys
import math

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print "Please enter: load dist dx dy"
        sys.exit()
    load = float(sys.argv[1])
    dist = float(sys.argv[2])
    dx = float(sys.argv[3])
    dy = float(sys.argv[4])

    fy = dist / dx * load
    angle = math.atan(dy / dx)
    print "Truss angle: " + str(angle * 180 / math.pi) + " deg"
    tension = fy / math.sin(angle)
    print "Force (consistent units): " + str(tension)

