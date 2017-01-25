#!/usr/bin/env python

import Basic 
import Units

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

def metrics(prop, motor):
    metrics = {}
    power = Units.fromHp(prop["hp"])
    metrics["power"] = motor["power"] / power * 100.0 - 100.0
    v = prop["rpm"] / motor["kv"]
    propcurrent = power / v
    metrics["current"] = motor["current"] / propcurrent * 100.0 - 100.0
    metrics["cells"] = v / 3.7
    metrics["mach"] = Basic.tipmach(prop["diameter"], prop["rpm"])
    metrics["power loading"] = prop["static thrust"] / power * 1000.0
    return metrics

def match(prop, motor):
    m = metrics(prop, motor)
    if m["power"] > 20 and m["current"] > 20 and m["cells"] <= 12:
	print "Prop: " + str(prop["diameter"])
	print "Motor: " + str(motor["kv"]) # + " " + str(motor[")
    	print "\tTip Mach: " + str(m["mach"])
    	print "\tPower: " + str(m["power"])
    	print "\tCurrent: " + str(m["current"])
	print "\tCells: " + str(m["cells"])
	print "\tPower Loading: " + str(m["power loading"])
	print "\tMotor weight: " + str(motor["weight"])
	print ""

if __name__ == "__main__":
    props = file2props("props.txt")
    motors = file2motors("motors.txt")
    for p in props:
        for m in motors:
	    match(p, m)

