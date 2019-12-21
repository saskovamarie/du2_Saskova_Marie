import json, quad_tree

# načtení dat geojson ze složky a uložení do proměnné
with open("input.geojson","r",encoding="utf-8") as f:
    data = json.load(f)
features = data["features"]

left,right,bottom,top = quad_tree.get_bbox(features)
mid_x = ((left + right)/2)
mid_y = ((bottom + top)/2)
len_x = abs(left - right)/2
len_y = abs(bottom - top)/2
output_list = []
output_list = quad_tree.quadtree(features,output_list,mid_x,mid_y,len_x,len_y)   #  seznam prvků obsahující navíc cluster_id

gj_structure = {"type": "FeatureCollection"}
gj_structure['features'] = output_list

# zapis souboru
with open("output.geojson", "w", encoding="utf-8") as f:
    json.dump(gj_structure, f, indent=2)
