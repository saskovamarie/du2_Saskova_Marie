import json, quad_tree

# načtení dat geojson ze složky a uložení do proměnné
with open ("input.geojson","r",encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]
points = features[:10]

bounding_box, points = quad_tree.edges(points)
quad_tree.building_quadtree(points,bounding_box)

