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