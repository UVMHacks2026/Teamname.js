# backend/player_repository.py

from backend.player_service import load_player

player_data = load_player(1)
def load_player(player_id):
    # query database
    # return PlayerData object

def save_player(player):
    # update database with player.balance etc