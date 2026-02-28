import sqlite3
import json

DB_PATH = "backend/game.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def load_player(player_id):
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

def save_player(player_id, name, balance):
    conn = get_connection()
    cursor = conn.cursor()

def load_player_map(player_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT map_state
        FROM users
        WHERE player_id = ?
    """, (player_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None or row["map_state"] is None:
        return None

    return row["map_state"]

def save_player_map(player_id, map_string):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET map_state = ?
        WHERE player_id = ?
    """, (map_string, player_id))

    conn.commit()
    conn.close()