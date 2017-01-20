#!/usr/bin/env python

def stress(M, y, I):
    """
    M is bending moment
    y is distance from bending axis
    I is area moment of inertia or second moment of area
    """
    return M * y / I

