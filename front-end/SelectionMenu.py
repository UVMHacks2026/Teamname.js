import pygame
from Building import Building
from Map import Map

class SelectionMenu:
    def __init__(self):
        self.color = (0, 0, 255)
        self.selectedNode = 0

    def setSelectedNode(self,mouseLoc):
        self.selectedNode = mouseLoc

    def drawNodeMenu(self,screen):
        #draw on top 
        if self.selectedNode > 10:
            pygame.draw.rect(screen, self.color, (0, 0, 1280, 200))
        
        #draw on bottom
        else:
            pygame.draw.rect(screen, self.color, (0, 720 - 200, 1280, 200))
        

