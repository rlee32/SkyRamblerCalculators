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

def current(prop, motor):
    power = Units.fromHp(prop["hp"])
    v = prop["rpm"] / motor["kv"]
    return power / v

def metrics(prop, motor):
    metrics = {}
    power = Units.fromHp(prop["hp"])
    metrics["power"] = motor["power"] / power * 100.0 - 100.0
    v = prop["rpm"] / motor["kv"]
    metrics["current"] = motor["current"] / current(prop, motor) * 100.0 - 100.0
    metrics["cells"] = v / 3.7
    metrics["mach"] = Basic.tipmach(prop["diameter"], prop["rpm"])
    metrics["power loading"] = prop["static thrust"] / prop["hp"]
    return metrics

def constrained(prop, motor):
    # TODO: fill in
    return True

def match(prop, motor):
    m = metrics(prop, motor)
    if m["power"] > 20 and m["current"] > 20 and m["cells"] <= 12:
	print "Prop: " + str(prop["diameter"])
	print "Motor: " + str(motor["kv"])
        print "\tTip Mach: " + str(m["mach"])
    	print "\tPower Margin: " + str(round(m["power"])) + "%"
    	print "\tCurrent Margin: " + str(round(m["current"])) + "%"
    	print "\tCurrent: " + str(current(prop, motor)) + " A"
	print "\tCells: " + str(m["cells"])
	print "\tPower Loading: " + str(m["power loading"]) + " lbf / hp"
	print "\tMotor weight: " + str(motor["weight"]) + " g"
	print ""

if __name__ == "__main__":
    props = file2props("props.txt")
    motors = file2motors("motors.txt")
    for p in props:
        for m in motors:
	    match(p, m)

