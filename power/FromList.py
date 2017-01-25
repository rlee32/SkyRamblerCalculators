#!/usr/bin/env python

import Basic 

def line2raw(line):
    return line.strip().split(",")

def line2prop(line):
    prop = {}
    raw = line2raw(line)
    prop["diameter"] = float(raw[0]) 
    prop["hp"] = float(raw[2]) 
    prop["rpm"] = float(raw[3]) 
    prop["static thrust"] = float(raw[4]) 
    return prop

def line2motor(line):
    motor = {}
    raw = line2raw(line)
    motor["kv"] = float(raw[0]) 
    motor["current"] = float(raw[1]) 
    motor["power"] = float(raw[2]) 
    motor["weight"] = float(raw[3]) 
    return motor

def iscomment(line):
    return line.strip() == "" or line.strip()[0] == "#" 

def file2props(filename):
    props = []
    with open(filename, 'r') as f:
        for line in f:
	    if not iscomment(line):
	        props.append(line2prop(line))
    return props

def file2motors(filename):
    motors = []
    with open(filename, 'r') as f:
        for line in f:
	    if not iscomment(line):
	        motors.append(line2motor(line))
    return motors

def config(hp, rpm, diam=None):
    if diam != None:
        tipSpeed = Units.fromInch(diam / 2.0) * Units.fromRpm(rpm)
        print "Tip Mach: " + str(tipSpeed / 343)
    cells = range(6, 13, 2)
    for c in cells:
        print str(c) + " cells:"
        print "\tkv:   " + str(kv(rpm, c))
        print "\tamps: " + str(current(hp, c))
    print "Power: " + str(Units.fromHp(hp)) + " W, " + str(hp) + " hp"

def match(prop, motor):
    print "Tip Mach: " + Basic.tipmach(prop["diameter"], prop["rpm"])
     

if __name__ == "__main__":
    props = file2props("props.txt")
    print props
    motors = file2motors("motors.txt")
    print motors

