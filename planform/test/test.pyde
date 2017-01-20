WindowDimension = 640
InchToPixels = 3

def setup():
    size(WindowDimension, WindowDimension)
    myDraw()

def PixelPlacement(x, y):
    c = (WindowDimension / 2, WindowDimension / 2)
    px = InchToPixels * x + WindowDimension / 2
    py = WindowDimension / 2 - InchToPixels * y
    return (px, py)

def Rotor(x, y, d):
    # fill(255)
    # stroke(0)
    (px, py) = PixelPlacement(x, y)
    D = InchToPixels * d
    ellipse(px, py, D, D)

def Strut(x1, y1, x2, y2):
    # fill(255)
    # stroke(0)
    (px1, py1) = PixelPlacement(x1, y1)
    (px2, py2) = PixelPlacement(x2, y2)
    line(px1, py1, px2, py2)
    
def myDraw():
    background(255)
    lateralDiam = 26.0
    lateralGap = 2.0
    
    lateralRadius = lateralDiam / 2.0
    lateralShift = lateralRadius + lateralGap / 2.0
    Rotor(-lateralShift, 0, lateralDiam)
    Rotor(lateralShift, 0, lateralDiam)
    print "Lateral strut length: " + str(2.0 * lateralShift)
    
    medialRadius = ceil(sqrt((lateralRadius ** 2.0) / 2.0))
    medialDiam = 2.0 * medialRadius
    medialGap = -5
    lateralGapMinor = 1
    
    medialShift = lateralRadius + medialGap + medialRadius
    lateralShiftMinor = medialRadius + lateralGapMinor / 2.0
    Rotor(-lateralShiftMinor, medialShift, medialDiam)
    Rotor(lateralShiftMinor, medialShift, medialDiam)
    Rotor(-lateralShiftMinor, -medialShift, medialDiam)
    Rotor(lateralShiftMinor, -medialShift, medialDiam)
    print "Medial strut length: " + str(2.0 * medialShift)
    print "Lateral strut minor length: " + str(2.0 * lateralShiftMinor)
    
    Strut(0, medialShift, 0, -medialShift)
    Strut(lateralShiftMinor, medialShift, -lateralShiftMinor, medialShift)
    Strut(lateralShiftMinor, -medialShift, -lateralShiftMinor, -medialShift)
    Strut(lateralShift, 0, -lateralShift, 0)