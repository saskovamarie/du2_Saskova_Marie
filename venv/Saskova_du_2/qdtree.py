
def edges (data):
    # points = data["features"]
    coord = []
    for point in data:
        souradnice = point["geometry"]["coordinates"]
        coord.append(souradnice)
    # sort podle X
    pointsX = sorted(coord, key=lambda x: x[0])
    left = pointsX[0]
    right = pointsX[-1]
    # sort podle Y
    pointsY = sorted(coord, key=lambda y: y[1])
    bottom = pointsY[0]
    top = pointsY[-1]
    # vypíše to hrany - pouze souřadnici x u left a right a pouze souřadnici y u top a bottom
    left_x = left[0]
    right_x = right[0]
    bottom_y = bottom[1]
    top_y = top[1]
    # vypocet středu
    mid_x = ((left_x+ right_x)/2)
    mid_y = ((bottom_y + top_y)/2)
    return mid_x,mid_y

def building_quadtree (data):
    if len(data)< 5: # konečná podmínka rekurze
        return(data)
    #features = data["features"]
    mid_x, mid_y = edges(data)
    NW = []
    NE = []
    SW = []
    SE = []

    for points in data:
        coords = points["geometry"]["coordinates"]
        if (coords[0] < mid_x) and (coords[1] < mid_y):
            SW.append(coords)
        if (coords[0] < mid_x) and (coords[1] > mid_y):
            NW.append(coords)
        if (coords[0] > mid_x) and (coords[1] < mid_y):
            SE.append(coords)
        if (coords[0] > mid_x) and (coords[1] > mid_y):
            NE.append(coords)

    # rekurzivní volání funkce
    #building_quadtree(SW)
    #building_quadtree(NW)
    #building_quadtree(SE)
    #building_quadtree(NE)
    print("sw:",SW)
    print("nw:",NW)
    print("se:",SE)
    print("ne:",NE)

