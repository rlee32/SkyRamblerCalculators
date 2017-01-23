#!/usr/bin/env python

"""
Reference: http://www.colorado.edu/engineering/CAS/courses.d/Structures.d/IAST.Lect09.d/IAST.Lect09.pdf
"""

import sys

def EnclosedArea(od, t):
    """
    od: outer dimension
    t: thickness
    """
    return (od - t) ** 2

def stress(T, od, t):
    """
    T: applied torsion
    od: outer dimension
    t: thickness
    """
    a = EnclosedArea(od, t)
    return T / 2.0 / t / a

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Input: outer dimension, thickness, load, moment arm"
        sys.exit()
    od = float(sys.argv[1])
    t = float(sys.argv[2])
    T = float(sys.argv[3]) * float(sys.argv[4])
    print "Stress (consistent with input units): " + str(stress(T, od, t))

