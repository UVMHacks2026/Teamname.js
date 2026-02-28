import pygame
from Building import Building
from Map import Map

class SelectionMenu:
    def __init__(self):
        self.color = (255, 196, 0)
        self.selectedNode = False
        self.grid = False

    def setSelectedNode(self,mouseLoc):
        self.selectedNode = mouseLoc

    def iniGrid(self,grid):
        self.grid = grid

    def drawNodeMenu(self):
        if self.selectedNode or self.grid:
            return False
        #draw on top 
        if self.selectedNode[1] > 10:
            pass
        #draw on bottom
        else:
            pygame.draw.rect(screen, self.color, (0, 720 - 200, 1280, 200))

