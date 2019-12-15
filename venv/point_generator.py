from random import uniform

# body generované jako floaty do čtverce (0,0), (1,1)
# bod uložen do seznamu dvojic
def random_square(npoints):
    points = []
    for _ in range (npoints):
        x = uniform(0,1)
        y = uniform(0,1)
        point = (x,y)
        points.append(point)
    return points

def circle(npoints):
    pass
