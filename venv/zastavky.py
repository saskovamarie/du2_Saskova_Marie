import json

with open("stops.json","r",encoding= "utf-8") as f:
    data = json.load(f)                     # v tomto okamžiku máme soubor uložený jako data a můžeme soubor zavřít, dále pracujeme bez odsazení

print(data)
print(len(data["features"]))

typ_dopravy = {1:"metro", 2:"tramvaj", 4:"autobus", 6:"tramvaj+autobus", 8:"lanovka", 16:"vlak", 20:"vlak+autobus", 32: "lod"}
seznam_P = []
n=0
features = data["features"]
for zast in features:
    pasmo = zast ["properties"]["ZAST_PASMO"]

    if pasmo == "P":
        n+=1
        seznam_P.append(zast)
        typ = zast ["properties"]["ZAST_DD"]
        prostredek = typ_dopravy[typ]
        zast["properties"]["ZAST_DD"] = prostredek

gj_structure = {"type":"FeatureCollection"}
gj_structure["features"] = seznam_P
with open("stops_out.json","w",encoding="utf-8") as f:
    json.dump(gj_structure,f,indent=2,ensure_ascii=False)

print(n)
print(len(seznam_P))





