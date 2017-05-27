#!/usr/bin/env python

"""
Reference:
http://www.colorado.edu/engineering/CAS/courses.d/Structures.d/IAST.Lect08.d/IAST.Lect08.Slides.pdf
"""

import sys

def polar(length, thickness):
    """
    Polar area moment of intertia.
    This assumes thin plate (length > ~5 * thickness).
    """
    return length * thickness ** 3 / 3.0

def stress(torque, length, thickness):
    """
    T: applied torsion
    length: length
    t: thickness
    """
    return torque * thickness / polar(length, thickness)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Input: plate length, thickness, load, moment arm"
        sys.exit()
    length = float(sys.argv[1])
    thickness = float(sys.argv[2])
    torque = float(sys.argv[3]) * float(sys.argv[4])
    print "Stress (consistent with input units): " + str(stress(torque, length, thickness))

