
class City:

    def __init__(self, mayor, year_established):
        self.mayor = mayor
        self.year_established = year_established
        self.buildings = list()
        

    def add_to_city(self, building):
        self.buildings.append(building)

        