import pygame
from Building import Building
from Shop import Shop
from Tower import Tower
from Walls import Walls
from Map import Map

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
map = Map()
TILE_SIZE = 40
build = Building()
map.addBuilding(build,(20,10))
shop = Shop()
map.addBuilding(shop,(20,17))

def getGridPos(mouse_pos, tile_size):
    x = mouse_pos[0] // tile_size
    y = mouse_pos[1] // tile_size
    return [x, y]


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = map.getGrid()
    mouseLoc = getGridPos(pygame.mouse.get_pos(), TILE_SIZE)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            node = grid[y][x]
            if node is None:
                #Draw green square
                pygame.draw.rect(screen, (0, 255, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
            else:
                node.draw(screen, TILE_SIZE)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
