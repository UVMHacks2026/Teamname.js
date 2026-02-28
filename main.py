# main.py

from backend.player_service import load_player, save_player
from frontend.player import Player
from frontend.game import run_game


def main():

    # Add functionality to get player username from database

    data = load_player(1)

    player = Player(
        id=data["id"],
        name=data["name"],
        map_data=data["map_data"],
        diamonds=data["diamonds"],
        gold=data["gold"],
        silver=data["silver"],
        iron=data["iron"],
        copper=data["copper"]
    )

    run_game(player)

    save_player(player)


if __name__ == "__main__":
    main()