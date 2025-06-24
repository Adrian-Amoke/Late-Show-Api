from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_migrate import Migrate
from server.config import DATABASE_URI, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return "Late Show API is running."

if __name__ == '__main__':
    app.run(debug=True, port=5555)
