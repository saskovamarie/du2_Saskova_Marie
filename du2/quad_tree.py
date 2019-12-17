
def coords (features):
    """
    :param features: vstupní seznam prvků vzniklých z geoJSON
    :return: vrací seznam, který obsahuje souřadnice x,y a prázdné místo dále využité pro cluster_id
    """
    points =[]
    for point in features:
        x = point['geometry']['coordinates'][0]
        y = point['geometry']['coordinates'][1]
        points.append([x,y,''])
    #print(points)
    return points

def edges(features):
    """
    :param features: vstupní seznam prvků vzniklých z geoJSON
    :return points: seznam, který obsahuje souřadnice x,y a prázdné místo dále využité pro cluster_id
    :return bounding box: seznam, který obsahuje souřadnice bodů left,right,bottom a top
    """
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
    bounding_box = [left,right,bottom,top]
    #print(bounding_box," \n",points )
    return bounding_box, points

def split_points(points,box,quadrant):
    """
    :param points: vstupní seznam bodů
    :param box: seznam obsahující souřadnice bodů left,right,bottom,up kvadrantu, pro který funkci počítáme
    :param quadrant: číslo kvadrantu, pro který počítáme
    :return: seznam
    """
    quad = []
    for point in points:
        id = point[2]
        id_cluster = id + str(quadrant)
        x = point[0]
        y = point[1]
        if box[0] <= x <= box[2] and box[1] <= y <= box[3]:
            quad.append([x,y,id_cluster])
        else:
            continue
    #print(quad)
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







