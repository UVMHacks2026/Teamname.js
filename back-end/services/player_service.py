# backend/player_service.py
def create_player_from_api_data(api_data):
    player = Player(api_data["id"], api_data["name"])
    resources = translate_financials_to_game_resources(api_data["transactions"])
    player.add_resources(resources)
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

        elif category == "Food and Drink":
            copper += int(amount // 10)

        elif category == "Travel":
            silver += int(amount // 50)

    return {
        "diamonds": diamonds,
        "gold": gold,
        "silver": silver,
        "iron": iron,
        "copper": copper
    }