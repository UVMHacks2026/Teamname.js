# backend/player_service.py
from frontend.Player import Player
from backend.database import get_connection
from frontend.Map import Map
import json

def create_player_from_api_data(api_data):
    player = Player(api_data["id"], api_data["name"])
    resources = translate_financials_to_game_resources(api_data["transactions"])
    player.mutate_resources(resources)
    return player

def translate_financials_to_game_resources(api_data):

    diamonds = 0
    gold = 0
    silver = 0
    iron = 0
    copper = 0

    if "income" in api_data:
        diamonds += int(api_data["income"] // 100)

    if "savings" in api_data:
        gold += int(api_data["savings"] // 10)

    # Investments → mid-tier resources
    if "investing" in api_data:
        silver += int(api_data["investments"] // 50)

    # Optional additional categories
    if "spending" in api_data:
        iron += int(api_data["spending"] // 75)

    if "paying_debt" in api_data:
        copper += int(api_data["paying_debt"] // 150)

    return {
        "diamonds": diamonds,
        "gold": gold,
        "silver": silver,
        "iron": iron,
        "copper": copper
    }

def update_player_from_object(player):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET
            gold = ?,
            diamonds = ?,
            silver = ?,
            iron = ?,
            copper = ?,
            map_state = ?
        WHERE player_id = ?
    """, (
        player.gold,
        player.diamonds,
        player.silver,
        player.iron,
        player.copper,
        player.map.to_db_format(),
        player.id
    ))

    conn.commit()
    conn.close()

def load_player_from_database(player_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE player_id = ?
    """, (player_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    player = Player(
        id = row["player_id"],
        gold = row["gold"],
        diamonds = row["diamonds"],
        silver = row["silver"],
        iron = row["iron"],
        copper = row["copper"]
    )

    if row["map_state"]:
        player.map = Map.from_db_format(row["map_state"])

    return player