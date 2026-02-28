import pygame
from frontend.Building import Building
from frontend.Map import Map
from frontend.Player import Player

class SelectionMenu:
    def __init__(self, player):
        self.color = (40, 40, 40)
        self.selectedNode = 0
        self.player = player

    def setSelectedNode(self,mouseLoc):
        self.selectedNode = mouseLoc

    def drawNodeMenu(self, screen, player):
        font = pygame.font.Font(None, 36)  # None = default font, 36 = size
        currencies = player.toString()
        text = font.render(currencies, True, (255, 255, 255))
        #draw on top
        if self.selectedNode > 10:
            pygame.draw.rect(screen, self.color, (0, 0, 1280, 200))
            screen.blit(text, (10, 10))

        #draw on bottom
        else:
            pygame.draw.rect(screen, self.color, (0, 720 - 200, 1280, 200))
            screen.blit(text, (10, 520))
        

