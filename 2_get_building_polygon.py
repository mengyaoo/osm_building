import os

from dotenv import load_dotenv

from models.buildings_generator import BuildingsGenerator

load_dotenv(os.path.join(os.getcwd(), '.env'))

if __name__ == '__main__':
    print('Start')
    generator = BuildingsGenerator()
    buildings = generator.generate()
    print('Done')
    with open('outputs/singapore_buildings1.geojson', 'w') as file_:
        file_.write(buildings)
