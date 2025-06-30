from flask import Flask, Blueprint, make_response, request
from models.appearance import Appearance
from flask_jwt_extended import jwt_required
from models.__init__ import db
from models.guest import Guest
from models.episode import Episode

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances')
@jwt_required
def create_appearance():
    data = request.get_json()
    
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    # Validate required fields
    if not all([rating, guest_id, episode_id]):
        return make_response({"error": "rating, guest_id, and episode_id are required"}), 400

    # Validate rating range
    if not (1 <= int(rating) <= 5):
        return make_response({"error": "rating must be between 1 and 5"}), 400

    # Validate foreign keys
    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest or not episode:
        return make_response({"error": "Invalid guest_id or episode_id"}), 404

    # Create the appearance
    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)

    db.session.add(appearance)
    db.session.commit()

    return make_response(appearance.to_dict(), 201)