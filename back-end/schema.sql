CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    level INTEGER DEFAULT 1,
    gold INTEGER DEFAULT 0,
    diamonds INTEGER DEFAULT 0,
    silver INTEGER DEFAULT 0,
    iron INTEGER DEFAULT 0,
    copper INTEGER DEFAULT 0,
    plaid_access_token TEXT
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    transaction_id TEXT UNIQUE,
    name TEXT,
    amount REAL,
    date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);