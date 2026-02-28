import sqlite3

DB_PATH = "backend/game.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_player(player_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("", (player_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "balance": row[2]
        }
    return None

def load_map(player_id, rows=18, cols=32):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT map_data FROM map_state WHERE player_id = ?", (player_id,))
    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    flat_map = row[0]

    return [
        list(flat_map[i*cols:(i+1)*cols])
        for i in range(rows)
    ]