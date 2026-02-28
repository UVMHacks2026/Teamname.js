import pygame
class Building:
    def __init__(self):
        self.level = 1
        self.untilNextLevel = 100
        self.isDestroyed = False
        self.location = [0,0]
        self.cost = 100
        self.color = (255, 251, 0)

    def upgradeBuilding(self, xp):
        if xp < self.untilNextLevel:
            print("not enough to upgrade")
        else:
            xp -= self.untilNextLevel
            self.updateCost(self.untilNextLevel)
            self.level += 1
            self.untilNextLevel *= 2
            print("building upgraded!")
        return xp
    
    def getUntilNextLevel(self):
        return self.untilNextLevel
    
    def reBuild(self,xp):
        if not self.isDestroyed:
            print("Building isnt destroyed")
        elif xp < 100:
            print("Not enough to rebuild")
        else:
            self.isDestroyed = False
            xp -= 100

    def draw(self, screen, tile_size):
        x = self.location[0] * tile_size
        y = self.location[1] * tile_size
        pygame.draw.rect(screen, self.color, (x, y, tile_size, tile_size))


    def getLocation(self):
        return self.location

    def setLocation(self,loc):
        self.location = loc

    def getLevel(self):
        return self.getLevel
    
    def updateCost(self,cost):
        self.cost = cost
    
