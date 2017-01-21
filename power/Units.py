#!/usr/bin/env python

import math

def fromRpm(rpm):
    # To rad/s
    return rpm / 60.0 * 2.0 * math.pi

def fromHp(hp):
    # To W
    return 745.7 * hp

def fromInch(inches):
    # To m
    return 0.0254 * inches