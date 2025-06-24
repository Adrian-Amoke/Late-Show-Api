from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.config import db
from server.models.appearance import Appearance

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify({'message': 'Appearance created successfully'}), 201
