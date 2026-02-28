# frontend/player.py
from frontend.Map import Map

class Player:
    def __init__(self, id, name, map_data,
                 diamonds, gold, silver, iron, copper):

        self.id = id
        self.name = name
        if map_data and "map_state" in map_data:
            self.map = Map.from_db_format(map_data["map_state"])
        else:
            self.map = None

        self.diamonds = diamonds
        self.gold = gold
        self.silver = silver
        self.iron = iron
        self.copper = copper

    def build(self, building_type, location, game_map):

        if not self.has_resources_for(building_type):
            return False
        game_map.build(building_type, location)
        return True


    def mutate_resources(self, resources_dict):
        self.diamonds = resources_dict["diamonds"]
        self.gold = resources_dict["gold"]
        self.silver = resources_dict["silver"]
        self.iron = resources_dict["iron"]
        self.copper = resources_dict["copper"]

    def has_resources_for(self, building_type):
        return self.diamonds >= building_type.cost.diamonds and \
               self.gold >= building_type.cost.gold and \
               self.silver >= building_type.cost.silver and \
               self.iron >= building_type.cost.iron and \
               self.copper >= building_type.cost.copper

    def to_dict(self):
        return {
            "player_id": self.id,
            "gold": self.gold,
            "diamonds": self.diamonds,
            "silver": self.silver,
            "iron": self.iron,
            "copper": self.copper,
            "map_state": self.map.to_db_format()
        }

    def update_from_dict(self, data):
        self.gold = data["gold"]
        self.diamonds = data["diamonds"]
        self.silver = data["silver"]
        self.iron = data["iron"]
        self.copper = data["copper"]

    def toString(self):
        currencies = f"Gold: {self.gold}, Diamonds: {self.diamonds}, Silver: {self.silver}, Iron: {self.iron}, Copper: {self.copper}"
        return currencies