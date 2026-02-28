import pygame
#from Building import Building
#from Shop import Shop
#from Tower import Tower
#from Walls import Walls
#from Map import Map
#from TownHall import TownHall
#from Player import Player
#from SelectionMenu import SelectionMenu
from frontend.Building import Building
from frontend.Shop import Shop
from frontend.Tower import Tower
from frontend.Walls import Walls
from frontend.Map import Map


def getGridPos(mouse_pos, tile_size):
    x = mouse_pos[0] // tile_size
    y = mouse_pos[1] // tile_size
    return [x, y]


def runPyGame(player):
    
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    nodeClicked = False
    map = Map()
    menu = SelectionMenu(player)
    TILE_SIZE = 40
    menuDrawn = False
    while running:
        grid = map.getGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #OnMouseClickButton
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseLoc = event.pos
                gridLoc = getGridPos(mouseLoc, TILE_SIZE)
                #gives just y value to selected node
                menu.setSelectedNode(gridLoc[1])
                nodeClicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    nodeClicked = False
                    menuDrawn = False

        #Draws menu
        if nodeClicked and not menuDrawn:
            menu.drawNodeMenu(screen)
            menuDrawn = True


        if nodeClicked == False:
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    node = grid[y][x]
                    if node is None:
                        #Draw green square
                        pygame.draw.rect(screen, (0, 0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(screen, (0, 255, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),1)
                    else:
                        node.draw(screen, TILE_SIZE)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
