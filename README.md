# osm_building

## Get Building Polygons
1_osm_building_polygon.txt: A sql script that queries OpenStreetMap using AWS Athena for building geometric information in a given bounding box.

2_get_buildings.py: Get the polygons and save the result as GeoJSON file in outputs
```bash
python 2_get_buildings.py 
``` 

## Get Building Centroids
1_osm_building_polygon.txt

2_get_building_centroid.txt: A sql script that generate building centroids from table created by query of 1_osm_building_polygon.

