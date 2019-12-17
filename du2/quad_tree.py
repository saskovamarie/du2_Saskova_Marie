

def coords (features):
    points =[]
    for point in features:
        x = point['geometry']['coordinates'][0]
        y = point['geometry']['coordinates'][1]
        points.append([x,y,''])
    print(points)
    return points

def edges(features):
    #print(len(features))
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
    #mid_x = ((left + right)/2)
    bounding_box = [left,right,bottom,top]
    #print(bounding_box)
    return bounding_box

def split_points(features,box,quadrant):
    quad = []
    for point in features:
        #point['properties']['id_cluster'] = ""
        #+str(quadrant)
        coordinates = point['geometry']['coordinates']
        x = coordinates[0]
        y = coordinates[1]
        if box[0] <= x <= box[2] and box[1] <= y <= box[3]:
            quad.append(x)
            quad.append(y)

    return quad

def building_quadtree (features, box,quadrant= 0):
    if len(features)< 5:
        output_list = []
        for point in features:
            output_list.append(point)
        print(output_list)

    else:
        mid = [((box[0] + box[1]) / 2),((box[2] + box[3]) / 2)]
        if quadrant == 0:
            box = box
        elif quadrant == 1:
            box = [box[0],mid[0],mid[1],box[2]]
        elif quadrant == 2:
            box = [mid[0],box[1],mid[1],box[3]]
        elif quadrant == 3:
            box = [box[0],mid[0],box[2],mid[1]]
        elif quadrant == 4:
            box = [mid[0],box[1],box[2],mid[1]]

        quad1 = split_points(features,box,1)
        quad2 = split_points(features,box,2)
        quad3 = split_points(features,box,3)
        quad4 = split_points(features,box,4)

        # rekurzivní volání funkce v každém bounding boxu
        building_quadtree(quad1,box,1)
        building_quadtree(quad2,box,2)
        building_quadtree(quad3,box,3)
        building_quadtree(quad4,box,4)







