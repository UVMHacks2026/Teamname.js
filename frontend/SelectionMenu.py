import pygame
from frontend.Building import Building
from frontend.Map import Map

class SelectionMenu:
    def __init__(self):
        self.color = (0, 0, 255)
        self.selectedNode = 0

    def setSelectedNode(self,mouseLoc):
        self.selectedNode = mouseLoc

    def drawNodeMenu(self,screen):
        font = pygame.font.Font(None, 36)  # None = default font, 36 = size
        Currencies = font.render(, True, (255, 255, 255))  # text, antialias, color
        #draw on top 
        if self.selectedNode > 10:
            pygame.draw.rect(screen, self.color, (0, 0, 1280, 200))

        #draw on bottom
        else:
            pygame.draw.rect(screen, self.color, (0, 720 - 200, 1280, 200))
        

