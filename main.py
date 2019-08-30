from building import Building, baseball_stadium, tennis_stadium, track_stadium, football_stadium, soccer_stadium
from city import City

nashville = City("Adam Knowles", "19")
nashville.add_to_city(baseball_stadium)
nashville.add_to_city(tennis_stadium)
nashville.add_to_city(track_stadium)
nashville.add_to_city(football_stadium)
nashville.add_to_city(soccer_stadium)
for building in nashville.buildings:
    print(f'{building.name}| address: {building.address}| owner: {building.owner}| stories: {building.stories}|')
    



















