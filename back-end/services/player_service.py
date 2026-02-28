# backend/player_service.py

from frontend.map import GameMap
import json

def create_player_from_api_data(api_data):
    player = Player(api_data["id"], api_data["name"])
    resources = translate_financials_to_game_resources(api_data["transactions"])
    player.mutate_resources(player, resources)
    return player

def translate_financials_to_game_resources(api_data):

    diamonds = 0
    gold = 0
    silver = 0
    iron = 0
    copper = 0

    # Income → high value currency
    if "income" in api_data:
        diamonds += int(api_data["income"] // 100)

    # Savings → basic resources
    if "savings" in api_data:
        copper += int(api_data["savings"] // 10)

    # Investments → mid-tier resources
    if "investments" in api_data:
        silver += int(api_data["investments"] // 50)

    # Optional additional categories
    if "spending" in api_data:
        iron += int(api_data["spending"] // 75)

    return {
        "diamonds": diamonds,
        "gold": gold,
        "silver": silver,
        "iron": iron,
        "copper": copper
    }

def load_map_for_game(player_id):
    from backend.database import load_player_map

    map_string = load_player_map(player_id)

    if map_string is None:
        return None

    return Map.from_db_format(map_string)