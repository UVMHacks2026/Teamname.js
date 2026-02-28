# backend/player_service.py

from  import get_player_row

class PlayerData:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

def load_player(player_id):
    row = get_player_row(player_id)

    if row is None:
        return None

    return PlayerData(
        id=row[0],
        name=row[1],
        balance=row[2]
    )