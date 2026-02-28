# frontend/player.py

class Player:
    def __init__(self, id, name, map_data,
                 diamonds, gold, silver, iron, copper):

        self.id = id
        self.name = name
        self.map_data = map_data

        self.diamonds = diamonds
        self.gold = gold
        self.silver = silver
        self.iron = iron
        self.copper = copper

    def build(self, building_type, location, game_map):
        game_map.build(building_type, location)

    def mutate_resources(self, resources):
        self.diamonds += resources.diamonds
        self.gold += resources.gold
        self.silver += resources.silver
        self.iron += resources.iron
        self.copper += resources.copper
