from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import SQLALCHEMY_DATABASE_URI, db
from server.controllers.auth_controller import auth_bp
from server.controllers.appearance_controller import appearance_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.guest_controller import guest_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret.secret'

jwt = JWTManager(app)

migrate = Migrate(app, db)
db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(appearance_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(guest_bp)

@app.route('/')
def index():
    return "Late Show Api"

if __name__ == '__main__':
    app.run(debug=True, port=5555)
