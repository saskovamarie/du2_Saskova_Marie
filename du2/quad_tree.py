def edges(data):
    # points = data["features"]
    coord = []
    for point in data:
        souradnice = point["geometry"]["coordinates"]
        coord.append(souradnice)
    # sort podle X
    coord.sort(key=lambda x: x[0])
    left = coord[0]
    right = coord[-1]
    # sort podle Y
    coord.sort(key=lambda y: y[1])
    bottom = coord[0]
    top = coord[-1]
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
    if len(data) < 10: # konečná podmínka rekurze
        return(data)
    #features = data["features"]
    mid_x, mid_y = edges(data)
    NW = []
    NE = []
    SW = []
    SE = []

    for points in data:
        coords = points["geometry"]["coordinates"] # podruhý dostávám jenom seznam - toto nefunguje!!
        x = coords[0]
        y = coords[1]
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
    print("sw:",SW)
    print("nw:",NW)
    print("se:",SE)
    print("ne:",NE)