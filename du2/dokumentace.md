#### DĚLENÍ ADRESNÍCH BODŮ POMOCÍ ALGORITMU QUADTREE

Program načte vstupní data ze souboru `input.geojson` a prvky ze souboru rozdělí do kvadrantů dokud není v jednotlivých kvadrantech méně než 50  prvků. Každému prvku přidá informaci o tom, do jakého kvadrantu patří a prvky vypíše do souboru `output.geojson`.

###### Vstupy:

- soubor ve formátu geoJSON jako FeatureCollection bodů, každý bod má své "properties" a "geometry" 

###### Výstupy:

- soubor ve formátu geoJSON `output.geojson`, který má stejné vlastnosti jako vstupní soubor, pouze je přidáno nové property - `cluster_id` s informací, do kterého kvadrantu byl bod zařazen

###### Funkce:

- *get_bbox(features)*

  do funkce vstupuje seznam prvků ve FeatureCollection vstupního souboru geoJSON, funkce vybere z každého prvku informaci o souřadnicích x, y, následně vybere souřadnice x s minimální hodnotou (left), s maximální hodnotou (right) a souřadnice y s minimální (bottom) a maximální hodnotou (top), funkce vrací tyto hodnoty jako bounding_box 

- *split_features(features, mid_x, mid_y)*

  funkce vytvoří pro každý kvadrant seznam, prvky rozdělí do jednotlivých kvadrantů podle souřadnic x,y a za cluster_id v properties přiřadí číslo kvadrantu 1-4 , pokud prvek ještě nemá cluster_id vytvoří jej, funkce vrací seznamy prvků v jednotlivých kvadrantech

- *quadtree(features, output_list, mid_x, mid_y, len_x, len_y, x = 0)*

  funkce mění hodnoty geografického středu podle kvadrantu pro který počítá (zadáno parametrem x), volá funkci *split_features* a následně je rekurzivně volaná na každý kvadrant, dokud není splněna podmínka délky vstupního seznamu (méně než 50 prvků)
