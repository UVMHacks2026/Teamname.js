from frontend.building import Building
from frontend.townhall import TownHall
from frontend.house import House
from frontend.shop import Shop
from frontend.tower import Tower
from frontend.walls import Wall

BUILDING_REGISTRY = {
    "TownHall": TownHall,
    "House": House,
    "Shop": Shop,
    "Tower": Tower,
    "Wall": Wall
}