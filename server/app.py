from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models.__init__ import db
from models.appearance import Appearance
from models.user import User
from models.guest import Guest
from models.episode import Episode

from controllers.appearance_controller import appearance_bp
from controllers.guest_controller import guest_bp
from controllers.episode_controller import episode_bp
from controllers.auth_controller import auth_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
app.json.compact = False

migrate = Migrate(app, db)
jwt = JWTManager(app)
db.init_app(app)
api = Api(app)

app.register_blueprint(guest_bp)
app.register_blueprint(appearance_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return f'<h1>Welcome to The Late Show</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)