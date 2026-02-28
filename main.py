# main.py

from backend.services import plaid_services, player_service
from frontend.Game import runPyGame
from frontend.Player import Player

def main():
    player = Player("id", "name", "map_data", 1000, 1000, 1000, 1000, 1000)
    runPyGame(player)
    # Add functionality to get player username from database
    #game_data = plaid_services.sync_plaid_for_player()
    #print(game_data)
   #player = player_service.create_player_from_game_data(game_data)


    #player_service.run_game(player)

    #player_service.save_player(player)
    #print(player)


if __name__ == "__main__":
    main()