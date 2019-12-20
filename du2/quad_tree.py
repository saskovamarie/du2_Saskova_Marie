

def get_bbox(features):
    """
    :param features: vstupní seznam prvků vzniklých z geoJSON
    :return bounding box: seznam, který obsahuje souřadnice bodů left,right,bottom a top
    """
    X = []
    Y = []
    for feature in features:
        x = feature['geometry']['coordinates'][0]
        y = feature['geometry']['coordinates'][1]
        X.append(x)
        Y.append(y)
    left = min(X)
    right = max(X)
    bottom = min(Y)
    top = max(Y)
    bounding_box = [left, right, bottom, top]
    #  print(bounding_box)
    return bounding_box

def split_features(features,mid_x, mid_y):
    """
    Funkce vytvoří seznam pro každý kvadrant, body podle x,y souřadnic rozdělí do jednotlivých kvadrantů a za cluster_id
    každého bodu přiřadí 1 - 4 podle kvadrantu, do kterého spadá (pokud prvek ještě nemá cluster_id vytvoří jej)
    :param features: vstupní seznam prvků vzniklých z geoJSON
    :param mid_x: střed na ose x, podle kterého jsou prvky rozděleny
    :param mid_y: střed na ose y, podle kterého jsou prvky rozděleny
    :return: seznamy prvků náležících do jednotlivých kvadrantů - quad1, quad2, quad3, quad4
    """
    quad1 = []
    quad2 = []
    quad3 = []
    quad4 = []
    for feature in features:
        if 'cluster_id' not in feature['properties']:
            feature['properties']['cluster_id'] = ''
        coords = feature['geometry']['coordinates']
        x = coords[0]
        y = coords[1]
        if x <= mid_x and y > mid_y:
            feature['properties']['cluster_id'] = str(feature['properties']['cluster_id']) + '1'
            quad1.append(feature)
        elif x > mid_x and y >= mid_y:
            feature['properties']['cluster_id'] = str(feature['properties']['cluster_id']) + '2'
            quad2.append(feature)
        elif x < mid_x and y <= mid_y:
            feature['properties']['cluster_id'] = str(feature['properties']['cluster_id']) + '3'
            quad3.append(feature)
        elif x >= mid_x and y < mid_y:
            feature['properties']['cluster_id'] = str(feature['properties']['cluster_id']) + '4'
            quad4.append(feature)
    return quad1, quad2, quad3, quad4

def quadtree (features, output_list, mid_x, mid_y, len_x, len_y, x = 0):
    """
    Funkce, mění hodnoty geometrického středu podle zadaného kvadrantu, pro který počítá, volá funkci split_features a
    následně je rekurzivně volaná na každý kvadrant dokud není splněna podmínka velikosti vstupního souboru
    :param features: vstupní seznam prvků
    :param output_list: výstupní seznam prvků
    :param mid_x: střed na ose x, dle kterého jsou rozděleny prvky
    :param mid_y: střed na ose y, dle kterého jsou rozděleny prvky
    :param len_x: vzdálenost na ose x, která odpovídá polovině vzdálenosti mezi krajními body x nadřazeného kvadrantu
    :param len_y: vzdálenost na ose y, která odpovídá polovině vzdálenosti mezi krajními body y nadřazeného kvadrantu
    :param x: číslo počítaného kvadrantu, defaultně nastaven na 0
    :return: výstupní output_list
    """
    if len(features) < 50:
        for point in features:
            output_list.append(point)
        return output_list

    if x != 0:
        if x == 1:
            mid_x = mid_x - len_x
            mid_y = mid_y + len_y
        if x == 2:
            mid_x = mid_x + len_x
            mid_y = mid_y + len_y
        if x == 3:
            mid_x = mid_x - len_x
            mid_y = mid_y - len_y
        if x == 4:
            mid_x = mid_x + len_x
            mid_y = mid_y - len_y

    quad1, quad2, quad3, quad4 = split_points(features, mid_x, mid_y)
    quadtree(quad1, output_list, mid_x, mid_y, len_x / 2, len_y / 2, x=1)
    quadtree(quad2, output_list, mid_x, mid_y, len_x / 2, len_y / 2, x=2)
    quadtree(quad3, output_list, mid_x, mid_y, len_x / 2, len_y / 2, x=3)
    quadtree(quad4, output_list, mid_x, mid_y, len_x / 2, len_y / 2, x=4)
    # rekurzivní volání funkce v každém bounding boxu
    return output_list
