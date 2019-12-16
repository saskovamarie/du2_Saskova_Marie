import json, quad_tree

# načtení dat geojson ze složky a uložení do proměnné
with open ("mrizka_new.json","r",encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]

bounding_box = quad_tree.edges(features)
quad_tree.building_quadtree(features,bounding_box)

