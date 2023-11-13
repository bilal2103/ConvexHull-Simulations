import math as mp
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0    #collinear
    elif val > 0:
        return 1    #clockwise
    else:
        return 2    #counter clockwise

def CheckLine(lineEndptA, lineEndptB, ptSubject):       #For brute force method, checking which side of the line do points lie on
    return (ptSubject.x - lineEndptA.x) * (lineEndptB.y - lineEndptA.y) - (ptSubject.y - lineEndptA.y) * (
                lineEndptB.x - lineEndptA.x)

def distance(p, q):
    return mp.sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)

def distSq(p1, p2):
    return ((p1.x - p2.x) * (p1.x - p2.x) +
            (p1.y - p2.y) * (p1.y - p2.y))

def left_most(points) -> int:                 #function for finding leftmost point
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn

def nextToTop(S):
    return S[-2]

def Add_Line(p1, p2, c, color):
    return c.create_line(p1.x, p1.y, p2.x, p2.y, fill=color)
def StringOrientation(p,q,r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return "Collinear"  # collinear
    elif val > 0:
        return "Clockwise"  # clockwise
    else:
        return "Counter clockwise"  # counter clockwise


def Collinear(p, q, r):
    if (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x) and
           q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y)):
        return True
    return False
def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if (o1 != o2) and (o3 != o4):
        return True
    if (o1 == 0) and Collinear(p1, p2, q1):
        return True
    if (o2 == 0) and Collinear(p1, q2, q1):
        return True
    if (o3 == 0) and Collinear(p2, p1, q2):
        return True
    if (o4 == 0) and Collinear(p2, q1, q2):
        return True
    return False
def AntoniosMethod(points):
    ax = float(points[1].x-points[0].x)     #P2x-P1x
    ay = float(points[1].y-points[0].y)     #P2y-P1y
    bx = float(points[2].x-points[3].x)     #Q1x-Q2x
    by = float(points[2].y - points[3].y)   #Q1y-Q2y
    cx = float(points[0].x-points[2].x)     #P1x-Q1x
    cy = float(points[0].y-points[2].y)     #P1y-Q1y
    alphaNum = float(by*cx - bx*cy)
    Denom = float(ay*bx-ax*by)

    if Denom > 0.0:
        if alphaNum < 0.0 or alphaNum > Denom:
            return -1,-1
    elif Denom < 0.0:
        if alphaNum > 0.0 or alphaNum < Denom:
            return -1,-1
    betaNum = ax*cy - ay*cx
    if Denom > 0.0:
        if betaNum < 0.0 or betaNum > Denom:
            return -1,-1
    elif Denom < 0.0:
        if betaNum > 0.0 or betaNum < Denom:
            return -1,-1
    if Denom == 0:
        #the given lines are collinear
        if doIntersect(points[0],points[1],points[2],points[3]) == False:
            return -1,-1
    detL1 = determinant(points[0].x,points[0].y,points[1].x,points[1].y)
    detL2 = determinant(points[2].x,points[2].y,points[3].x,points[3].y)
    detL1andL2 = determinant(-ax,-ay,bx,by)
    x = determinant(detL1,-ax,detL2,bx)/detL1andL2
    y = determinant(detL1,-ay,detL2,by)/detL1andL2
    return x,y

def determinant(a,b,c,d):
    return float(a*d-b*c)

