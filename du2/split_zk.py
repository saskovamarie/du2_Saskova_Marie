import json, quad_tree

# načtení dat geojson ze složky a uložení do proměnné
with open("mrizka3.json","r",encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]

print(len(features))

box = quad_tree.edges(features)
mid_x = ((box[0] + box[1])/2)
mid_y = ((box[2] + box[3])/2)
len_x = abs(box[0] - box[1])/2
len_y = abs(box[2] - box[3])/2
output_list = []
output_list = quad_tree.quadtree(features,output_list,mid_x,mid_y,len_x,len_y)
print(output_list)
print("delka:", len(output_list))

gj_structure = {"type": "FeatureCollection"}
gj_structure['features'] = output_list

# zapis souboru
with open("mrizka3_output2.geojson", "w", encoding="utf-8") as f:
    json.dump(gj_structure, f, indent=2)
