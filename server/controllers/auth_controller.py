from flask import Blueprint, request, make_response
from models.user import User
from models.__init__ import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return make_response({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return make_response({"error": "Username already exists"}), 400

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return make_response({"message": "User registered successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return make_response({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=user.id)
    return make_response({"access_token": access_token}), 200