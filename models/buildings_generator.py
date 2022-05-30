from io import StringIO

import boto3
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon


class BuildingsGenerator(object):

    def __init__(self):
        pass



    @staticmethod
    def create_polygon(way):
        node_list = list(zip(way.lon, way.lat))
        return Polygon(node_list) if len(node_list) >= 3 \
            else None

    def generate(self):
        all_buildings = gpd.GeoDataFrame()
        results = pd.read_csv('data/Singapore_data.csv', encoding='utf-8')
        ways = results.groupby(by=['building_id', 'way_id'])
        for _, way in ways:
            polygon = self.create_polygon(way)
            if polygon:
                metadata = way.iloc[0]
                building_gdf = gpd.GeoDataFrame(
                    [[
                        metadata['building_id'],
                        metadata['name'],
                        metadata['amenity'],
                        metadata['shop'],
                        metadata['aeroway'],
                        metadata['building'],
                        metadata['leisure'],
                        metadata['office'],
                        metadata['healthcare'],
                        metadata['craft'],
                        metadata['emergency'],
                        metadata['historic'],
                        metadata['man_made'],
                        metadata['military'],
                        metadata['place'],
                        metadata['power'],
                        metadata['public_transport'],
                        metadata['railway'],
                        metadata['sport'],
                        metadata['tourism'],
                        metadata['landuse'],
                        polygon
                    ]],
                    columns=[
                        'building_id',
                        'name',
                        'amenity',
                        'shop',
                        'aeroway',
                        'building',
                        'leisure',
                        'office',
                        'healthcare',
                        'craft',
                        'emergency',
                        'historic',
                        'man_made',
                        'military',
                        'place',
                        'power',
                        'public_transport',
                        'railway',
                        'sport',
                        'tourism',
                        'landuse',
                        'geometry'
                    ]
                )
                all_buildings = all_buildings.append(building_gdf)
            
        return all_buildings.to_json(ensure_ascii=False)
