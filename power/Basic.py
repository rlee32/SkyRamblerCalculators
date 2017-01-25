#!/usr/bin/env python

import math
import Units

def volts(cells):
    return 3.7 * cells

def kv(rpm, cells):
    return rpm / volts(cells)

def current(hp, cells):
    return Units.fromHp(hp) / volts(cells)

def tipmach(diam, rpm):
    tipSpeed = Units.fromInch(diam / 2.0) * Units.fromRpm(rpm)
    return tipSpeed / 343.0

def config(hp, rpm, diam=None):
    if diam != None:
        print "Tip Mach: " + tipmach(diam, rpm)
    cells = range(6, 13, 2)
    for c in cells:
        print str(c) + " cells:"
        print "\tkv:   " + str(kv(rpm, c))
        print "\tamps: " + str(current(hp, c))
    print "Power: " + str(Units.fromHp(hp)) + " W, " + str(hp) + " hp"

if __name__ == "__main__":
    config(2.0 / 0.8, 8000, 18)

