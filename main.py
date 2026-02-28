# main.py

from backend.player_service import load_player, save_player
from frontend.player import Player
from frontend.game import run_game


def main():

    # Add functionality to get player username from database
    result = sync_plaid_for_player()

    game_data = translate_financials_to_game_resources(result)
    player = make_player_from_game_data(game_data)


    run_game(player)

    save_player(player)


if __name__ == "__main__":
    main()