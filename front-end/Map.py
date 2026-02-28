from Building import Building
class Map:
    MAX_BUILDING = 5
    def __init__(self):
        self.buildings = []

    def addBuilding(self, building):
        self.buildings.append(building)

    def getNumBuildings(self):
        return len(self.buildings)
    
    def getGold(self):
        return self.gold


    
