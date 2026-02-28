from backend.player_repository import load_player
from frontend.player import Player

data = load_player(player_id)

player = Player(
    id=data.id,
    name=data.name,
    balance=data.balance
)