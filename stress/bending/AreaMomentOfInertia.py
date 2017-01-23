#!/usr/bin/env python

def rectangle(b, h):
    """
    b is the width (along bending axis)
    h is the height (perpendicular to bending axis)
    """
    return b * (h ** 3.0) / 12.0

def rectangleDisplaced(b, h, d):
    """
    d is displacement of bending axis from rectangle's centroid
    """
    a = b * h
    i0 = rectangle(b, h)
    return i0 + a * (d ** 2.0)

def squareTube(od, t):
    """
    od is outer dimension
    t is thickness
    """
    side = rectangle(t, od - 2.0 * t)
    top = rectangleDisplaced(od, t, od / 2.0 - t / 2.0)
    return 2.0 * side + 2.0 * top

