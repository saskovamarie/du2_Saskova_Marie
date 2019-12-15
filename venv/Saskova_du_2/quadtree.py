
# vypocet b_boxu

def quad_tree(points,souradnice_x,souradnice_y):
    if len(points) <= 50:
        print(points)
        return points
    for point in points:
        souradnice = point["geometry"]["coordinates"]
        x = souradnice[0]
        y = souradnice[1]
        souradnice_x.append(x)
        souradnice_y.append(y)
    souradnice_x.sort()
    souradnice_y.sort()
    print(souradnice_x)
    print(souradnice_y)
    kb_x1 = souradnice_x[0]
    kb_x2 = souradnice_x[len(souradnice_x) - 1]
    kb_y1 = souradnice_y[0]
    kb_y2 = souradnice_y[len(souradnice_y) - 1]
    print(kb_x1, kb_x2, kb_y1, kb_y2)
    mid_x = (kb_x1 + kb_x2) / 2
    mid_y = (kb_y1 + kb_y2) / 2
    print(mid_x, mid_y)
    cluster_id = 0
    SW = []
    SE = []
    NW = []
    NE = []
    for sourad in points:
        sour = sourad["geometry"]["coordinates"]
        if (sour[0] < mid_x) and (sour[1] < mid_y):
            SW.append(sour)
            print("sw:",SW,)
            quad_tree(SW,souradnice_x,souradnice_y)
        if (sour[0] < mid_x) and (sour[1] > mid_y):
            NW.append(sour)
            print("nw:", NW,)
            quad_tree(NW,souradnice_x,souradnice_y)
        if (sour[0] > mid_x) and (sour[1] < mid_y):
            SE.append(sour)
            print("se:",SE,)
            quad_tree(SE,souradnice_x,souradnice_y)
        if (sour[0] > mid_x) and (sour[1] > mid_y):
            NE.append(sour)
            print("ne:",NE,)
            quad_tree(NE,souradnice_x,souradnice_y)

    #print(SW)
    #print(SE)
    #print(NW)
    #print(NE)

with open ("input.geojson","r",encoding="utf-8") as f:
    data = json.load(f)

points = data["features"]
souradnice_x = []
souradnice_y = []
quad_tree(points,souradnice_x,souradnice_y)
