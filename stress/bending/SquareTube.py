#!/usr/bin/env python

import sys
import AreaMomentOfInertia as amoi
import ElasticStructure as es

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Input: outer dimension, thickness, load, distance"
        sys.exit()
    od = float(sys.argv[1])
    i = amoi.squareTube(od, float(sys.argv[2]))
    m = float(sys.argv[3]) * float(sys.argv[4])
    y = od / 2
    print "Stress (consistent with input units): " + str(es.stress(m, y, i))

