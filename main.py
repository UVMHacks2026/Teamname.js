# main.py

from backend.services import plaid_services, player_service
from frontend.Game import runPyGame
from frontend.Player import Player

def main():

    # Add functionality to get player username from database
    game_data = plaid_services.sync_plaid_for_player()
    player = player_service.create_player_from_game_data(game_data, 00, "Player1")
    print(player)

    player_service.run_game(player)

    player_service.save_player(player)



if __name__ == "__main__":
    main()