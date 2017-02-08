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
    diam = 20.0
    r = diam / 2.0
    lateralGap = 1.0
    lateralSep = 20.0
    medialGap = 1
    medialSep = -3
    
    lateralRadius = diam / 2.0
    lateralShift = lateralRadius + lateralSep / 2.0
    lateralShiftY = lateralRadius + lateralGap / 2.0
    Rotor(-lateralShift, lateralShiftY, diam)
    Rotor(lateralShift, lateralShiftY, diam)
    Rotor(-lateralShift, -lateralShiftY, diam)
    Rotor(lateralShift, -lateralShiftY, diam)
    print "Lateral strut length: " + str(2.0 * lateralShift)
    
    medialShift = r + medialSep / 2.0
    x = r + medialGap / 2.0
    Rotor(-x, medialShift, diam)
    Rotor(x, medialShift, diam)
    Rotor(-x, -medialShift, diam)
    Rotor(x, -medialShift, diam)
    print "Medial strut length: " + str(2.0 * medialShift)
    # print "Lateral strut minor length: " + str(2.0 * lateralShiftMinor)
    
    # Strut(0, medialShift, 0, -medialShift)
    # Strut(lateralShiftMinor, medialShift, -lateralShiftMinor, medialShift)
    # Strut(lateralShiftMinor, -medialShift, -lateralShiftMinor, -medialShift)
    # Strut(lateralShift, 0, -lateralShift, 0)