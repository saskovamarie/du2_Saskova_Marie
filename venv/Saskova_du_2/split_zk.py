import json, qdtree

# načtení dat geojson ze složky a uložení do proměnné
with open ("input.geojson","r",encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]
qdtree.building_quadtree(features)

