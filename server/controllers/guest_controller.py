from flask import Flask, Blueprint, make_response
from models.guest import Guest

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests')
def get_guests():
    guests = [guest.to_dict() for guest in Guest.query.all()]
    if guests:
        return make_response(guests, 200)