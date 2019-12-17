import json, quad_tree

# načtení dat geojson ze složky a uložení do proměnné
with open ("input.geojson","r",encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]
points = features[:10]
print(points)
quad_tree.coords(points)
#bounding_box= quad_tree.edges(points)
#quad_tree.building_quadtree(points,bounding_box)

