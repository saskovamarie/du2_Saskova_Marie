def coords (features):
    points =[]
    for point in features:
        coordinates = point['geometry']['coordinates']
        points.append(coordinates)
        return points

def edges(features):
    print(len(features))
    # points = data["features"]
    points = coords(features)
    # seřazení podle osy X
    pointsX = sorted(points, key=lambda x: x[0])
    left = pointsX[0][0]
    right = pointsX[-1][0]
    # sort podle Y
    pointsY = sorted(points,key=lambda y: y[1])
    bottom = pointsY[0][1]
    top = pointsY[-1][1]
    # vypíše to hrany - pouze souřadnici x u left a right a pouze souřadnici y u top a bottom

    # vypocet středu
    mid_x = ((left + right)/2)
    mid_y = ((bottom + top)/2)
    print(mid_x,mid_y)
    return mid_x,mid_y

def building_quadtree (features):
    if len(features) < 5: # konečná podmínka rekurze
        # změna id_cluster
        return(features)
    #features = data["features"]
    mid_x, mid_y = edges(features)
    NW = []
    NE = []
    SW = []
    SE = []


    points = coords(features)
    for point in points:
        x = point[0]
        print(x)
        y = point[1]
        print(y)
        if (x < mid_x) and (y < mid_y):
            SW.append(coords)
        if (x < mid_x) and (y > mid_y):
            NW.append(coords)
        if (x > mid_x) and (y < mid_y):
            SE.append(coords)
        if (x > mid_x) and (y > mid_y):
            NE.append(coords)

    building_quadtree(SW)
    building_quadtree(NW)
    building_quadtree(SE)
    building_quadtree(NE)
    print("sw:",SW, "délka:",len(SW))
    print("nw:",NW,"délka:",len(NW))
    print("se:",SE,"délka:",len(SE))
    print("ne:",NE,"délka:",len(NE))