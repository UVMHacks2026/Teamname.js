from flask import Flask
from database import init_db

app = Flask(__name__)

init_db()

if __name__ == "__main__":
    app.run(debug = True)