class Building:
    def __init__(self):
        self.level = 1
        self.untilNextLevel = 100
        self.isDestroyed = False

    def upgradeBuilding(self, xp):
        if xp < self.untilNextLevel:
            print("not enough to upgrade")
        else:
            xp -= self.untilNextLevel
            self.level += 1
            self.untilNextLevel *= 2
            print("building upgraded!")
        return xp
    
    def getLevel(self):
        return self.getLevel
    
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


