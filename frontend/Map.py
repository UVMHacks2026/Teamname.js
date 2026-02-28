from Building import Building
import json

class Map:
    #X,Y
    CoordinatePlane = [1280, 720]
    #nodes will be 32 /18 (x/40 y/40)
    MAX_BUILDING = 5
    def __init__(self):
        self.buildings = []
        self.grid = [[None for x in range(33)] for y in range(19)]


    def getNumBuildings(self):
        return len(self.buildings)
    
    def checkOccupied(self, loc):
        for b in self.buildings:
            if self.grid[loc[1]][loc[0]] is not None:
                return True
        return False 
    
    #LOC + [X][Y]
    def addBuilding(self, Building, loc):
        if self.checkOccupied(loc) or not (0 <= loc[0] <= 32 and 0 <= loc[1] <= 18):
            return False
            #occupied return false
        #saves building location 
        Building.setLocation(loc)
        #adds building to grid
        self.grid[loc[1]][loc[0]] = Building
        self.buildings.append(Building)
        return True 
    
    def getGrid(self):
            return self.grid

    def to_db_format(self):
        return json.dumps([
            [cell.to_dict() if cell else None for cell in row]
            for row in self.grid
        ])

    @classmethod
    def from_db_format(cls, json_string):

        if json_string is None:
            return cls([])

        data = json.loads(json_string)

        grid = []

        for row in data:
            new_row = []

            for cell in row:
                if cell is None:
                    new_row.append(None)
                else:
                    new_row.append(Building.from_dict(cell))

            grid.append(new_row)

        return cls(grid)