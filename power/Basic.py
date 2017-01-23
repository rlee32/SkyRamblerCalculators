#!/usr/bin/env python

import math
import Units

def volts(cells):
    return 3.7 * cells

def kv(rpm, cells):
    return rpm / volts(cells)

def current(hp, cells):
    return Units.fromHp(hp) / volts(cells)

def config(hp, rpm, diam=None):
    if diam != None:
        tipSpeed = Units.fromInch(diam / 2.0) * Units.fromRpm(rpm)
        print "Tip Mach: " + str(tipSpeed / 343)
    cells = range(2, 11)
    for c in cells:
        print str(c) + " cells:"
        print "\tkv:   " + str(kv(rpm, c))
        print "\tamps: " + str(current(hp, c))
    print "Power: " + str(Units.fromHp(hp)) + " W, " + str(hp) + " hp"

if __name__ == "__main__":
    config(1.8 / 0.8, 6000, 20)

