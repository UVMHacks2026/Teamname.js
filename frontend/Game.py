import pygame

from frontend.Houses import Houses
#from Building import Building
#from Shop import Shop
#from Tower import Tower
#from Walls import Walls
#from Map import Map
#from TownHall import TownHall
#from Player import Player
from frontend.SelectionMenu import SelectionMenu
from frontend.Building import Building
from frontend.Shop import Shop
from frontend.Tower import Tower
from frontend.TownHall import TownHall
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
                if event.key == pygame.K_z:
                    if player.diamonds >= 10:
                        gridLoc = getGridPos(mouseLoc, TILE_SIZE)
                        map.grid[gridLoc[0]][gridLoc[1]] = TownHall()
                        map.grid[gridLoc[0]][gridLoc[1]].location = gridLoc
                        player.diamonds -= 10

                if event.key == pygame.K_x:
                    if player.gold >= 10:
                        gridLoc = getGridPos(mouseLoc, TILE_SIZE)
                        map.grid[gridLoc[0]][gridLoc[1]] = Tower()
                        map.grid[gridLoc[0]][gridLoc[1]].location = gridLoc
                        player.gold -= 10


                if event.key == pygame.K_c:
                    if player.silver >= 10:
                        gridLoc = getGridPos(mouseLoc, TILE_SIZE)
                        map.grid[gridLoc[0]][gridLoc[1]] = Shop()
                        map.grid[gridLoc[0]][gridLoc[1]].location = gridLoc
                        player.silver -= 10

                if event.key == pygame.K_v:
                    if player.iron >= 10:
                        gridLoc = getGridPos(mouseLoc, TILE_SIZE)
                        map.grid[gridLoc[0]][gridLoc[1]] = Houses()
                        map.grid[gridLoc[0]][gridLoc[1]].location = gridLoc
                        player.iron -= 10


                if event.key == pygame.K_b:
                    if player.copper >= 10:
                        gridLoc = getGridPos(mouseLoc, TILE_SIZE)
                        map.grid[gridLoc[0]][gridLoc[1]] = Walls()
                        map.grid[gridLoc[0]][gridLoc[1]].location = gridLoc
                        player.copper -= 10


        #Draws menu
        if nodeClicked and not menuDrawn:
            menu.drawNodeMenu(screen, player)
            menuDrawn = True


        if nodeClicked == False:
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    node = grid[y][x]
                    if node is None:
                        #Draw green square
                        pygame.draw.rect(screen, (40, 160, 40), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(screen, (50, 150, 50), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),1)
                    else:
                        node.draw(screen, TILE_SIZE)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
