from Building import Building

class Shop(Building):
    def __init__(self):
        super().__init__()
        self.color = (0, 0, 255)
        buildingSize = 40
        
