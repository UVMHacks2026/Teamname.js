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

    for t in transactions:
        amount = t["amount"]
        category = t["category"][0]

        if category == "Income":
            diamonds += int(amount // 100)

        elif category == "Savings":
            copper += int(amount // 10)

        elif category == "Investments":
            silver += int(amount // 50)

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