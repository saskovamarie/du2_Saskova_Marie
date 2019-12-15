import json, turtle, sys, os.path
from operator import itemgetter


def open_geojson(file_name):
    """
    funkce pro otevření geojsonu
    :param file_name: absulutní/relativní cesta k souboru
    :return: otevřený soubor
    """
    if os.path.isfile(file_name):  # pokud soubor existuje
        try:
            with open(file_name, encoding="utf-8") as in_f:  # zkus otevřít
                open_file = json.load(in_f)
        except Exception as e:
            print(e)
            print(file_name + 'soubor je poškozený, či se nejedná o korektní geojson')
            exit(1)
    else:
        print(file_name + 'soubor neexistuje')
        exit(1)
    return open_file


def build_quadtree(in_points, out_points, bbox, quadrant=0, size=50):
    """
    rekurzivní funkce pro dělení bodů do kvadrantů
    :param in_points: seznam vstupních bodů
    :param out_points: prázdný seznam pro tvorbu výstupního seznamu bodů
    :param bbox: bounding box bodů
    :param quadrant: číslo kvadrantu
    :param size: maximalní velikost skupiny
    :return: out_points = seznam bodů včetně jejich unikátního kódu skupiny
    """
    if len(in_points) <= size:  # konečná podmínka rekurze
        draw_bbox(bbox)
        for point in in_points:
            out_points.append(point)  # tvorba výstupniho seznamu bodů
        return
    else:
        middle = [(bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2]  # střed bboxu
        quad_1 = [middle[0], middle[1], bbox[2], bbox[3]]  # bbox prvního kvadrantu
        quad_2 = [middle[0], bbox[1], bbox[2], middle[1]]  # bbox druhého kvadrantu
        quad_3 = [bbox[0], bbox[1], middle[0], middle[1]]  # bbox třeti´ího kvadrantu
        quad_4 = [bbox[0], middle[1], middle[0], bbox[3]]  # bbox čtvtého kvadrantu
        P1 = select_points(in_points, quad_1, 1)  # body v prvním kvadrantu
        P2 = select_points(in_points, quad_2, 2)
        P3 = select_points(in_points, quad_3, 3)
        P4 = select_points(in_points, quad_4, 4)
        draw_bbox(bbox)
        build_quadtree(P1, out_points, quad_1, 1, size)  # rekuzivní voláni funkce pro první kvadrant
        build_quadtree(P2, out_points, quad_2, 2, size)
        build_quadtree(P3, out_points, quad_3, 3, size)
        build_quadtree(P4, out_points, quad_4, 4, size)
    return out_points


def select_points(points, boundaries, quad):
    """
    funkce pro výběr bodů v kvadrantu a tvorby jedinečného ID skupiny
    :param points: seznam vstupních bodů
    :param boundaries: hranice výběru = bbox
    :param quad: číslo kvadrantu pro tvorbu kodu
    :return: seznam bodu včetně ID skupiny
    """
    P = []
    for point in points:
        ID = point[0]
        x = point[1]
        y = point[2]
        old_code = point[3]
        new_code = old_code + str(quad)  # postupná úprava ID skupiny, podle kvadrantu a hloubky rekurze
        if boundaries[0] <= x <= boundaries[2] and boundaries[1] <= y <= boundaries[3]:
            P.append([ID, x, y, new_code])
        else:
            continue
    return P


def compute_bbox(data):
    """
    funkce která počítá rozměry bounding boxu a zároveň vytváří seznam bodů ze vstupního geojsonu
    :param data: otevřený vstupní geojson
    :return: seznam bodů, rozměry bounding boxu
    """
    points = []
    for i, feature in enumerate(data['features'], 1):  # tvorba seznamu vstupních bodů
        xy = feature['geometry']['coordinates']
        points.append([i, xy[0], xy[1], ""])
        if i == 1:  # hledáni bounding boxu všech bodů
            min_x = xy[0]
            max_x = xy[0]
            min_y = xy[1]
            max_y = xy[1]
        else:
            if xy[0] < min_x:
                min_x = xy[0]
            if xy[0] > max_x:
                max_x = xy[0]
            if xy[1] < min_y:
                min_y = xy[1]
            if xy[1] > max_y:
                max_y = xy[1]
    bbox = [min_x, min_y, max_x, max_y]
    return points, bbox


def draw_bbox(bbox):
    """"
    funkce pro vykreslení aktuálního kvadrantu
    :param bbox: souřadnice pro vykresleni
    """
    turtle.speed(0)
    turtle.ht()
    turtle.up()
    turtle.setpos(bbox[0], bbox[1])
    turtle.down()
    turtle.forward(abs(bbox[2] - bbox[0]))
    turtle.left(90)
    turtle.forward(abs(bbox[3] - bbox[1]))
    turtle.left(90)
    turtle.forward(abs(bbox[2] - bbox[0]))
    turtle.left(90)
    turtle.forward(abs(bbox[3] - bbox[1]))
    turtle.left(90)
    turtle.up()


def draw_points(points):
    """
    funkce pro vykreslení všech bodů
    :param points: seznam bodů
    """
    turtle.setworldcoordinates(bbox[0], bbox[1], bbox[2], bbox[3])  # úprava zobrazovacího okna
    turtle.speed(0)
    turtle.ht()
    turtle.tracer(50, 1)  # uprava "rychlosti" vykreslování
    for i in range(len(points)):  # vykreslení bodu
        turtle.up()
        turtle.setpos(points[i][1], points[i][2])
        turtle.down()
        turtle.dot(5, "blue")


if len(sys.argv) != 3:  # ošetření počtu vstupních argumentů
    print('málo nebo moc argumentů')
    exit(3)
else:
    data = open_geojson(sys.argv[1])

out_file = sys.argv[2]

points, bbox = compute_bbox(data)

draw_points(points)

group_size = 50  # maximální velikost skupiny

if len(points) <= group_size:  # ošetření podminky, kdy je velikost skupiny větší nebo rovna velikosti všech bodů
    draw_bbox(bbox)
    for i, value in enumerate(data['features'], 0):
        value['properties']['cluster_id'] = 0
else:
    out_points = []
    out_points = build_quadtree(points, out_points, bbox, size=group_size)
    sorted_points = sorted(out_points, key=itemgetter(0))  # seřazení bodů podle jejich ID
    for i, value in enumerate(data['features'], 0):
        value['properties']['cluster_id'] = sorted_points[i][3]  # přiřazení kódu skupiny výstupím bodům

dir_file = os.path.dirname(os.path.abspath(out_file))  # zjištění absolutní cesty ke výstupnímu souboru
if os.access(dir_file, os.W_OK):  # oveření, zda cesta existuje a zda je možný zápis
    with open(out_file, 'w') as out:  # uložení výstupního souboru
        json.dump(data, out)
    output = open_geojson(out_file)  # test otevření výstupniho souboru
else:
    print('cesta k výstupnimu souboru neexistuje, nebo není možný zápis')

turtle.exitonclick()