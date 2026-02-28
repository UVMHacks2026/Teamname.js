from backend.database import get_connection
from frontend.map import Map

def save_map(player_id, game_map):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET map_state = ?
        WHERE player_id = ?
    """, (
        game_map.to_db_format(),
        player_id
    ))

    conn.commit()
    conn.close()


def load_map(player_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT map_state
        FROM users
        WHERE player_id = ?
    """, (player_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return Map.from_db_format(row["map_state"])