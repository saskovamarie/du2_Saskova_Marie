

def coords (features):
    points =[]
    for point in features:
        coordinates = point['geometry']['coordinates']
        points.append(coordinates)
    print(points)
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
    bounding_box = [mid_x,mid_y,left,right,bottom,top]
    return bounding_box

def split_points(points,box):

    NW = []
    NE = []
    SW = []
    SE = []
    for point in points:
        point['properties']['id_cluster']=''
        coordinates = point['geometry']['coordinates']
        x = coordinates[0]
        y = coordinates[1]
        if (x < box[0]) and (y < box[1]):
            point['properties']['id_cluster'] += '1'
            SW.append(point)
        if (x < box[0]) and (y > box[1]):
            point['properties']['id_cluster'] += '2'
            NW.append(point)
        if (x > box[0]) and (y < box[1]):
            point['properties']['id_cluster'] += '3'
            SE.append(point)
        if (x > box[0]) and (y > box[1]):
            point['properties']['id_cluster'] += '4'
            NE.append(point)
    return NW,NE,SW,SE

def building_quadtree (input_points, box):
    if len(input_points)< 5:
        return(input_points)

    NW,NE,SW,SE = split_points(input_points,box)


    building_quadtree(SW,box)
    building_quadtree(NW,box)
    building_quadtree(SE,box)
    building_quadtree(NE, box)
    print("sw:",SW, "délka:",len(SW))
    print("nw:",NW,"délka:",len(NW))
    print("se:",SE,"délka:",len(SE))
    print("ne:",NE,"délka:",len(NE))