from flask import Blueprint, make_response, request
from models.episode import Episode
from models.__init__ import db

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes')
def episodes():
    episodes = [episode.to_dict() for episode in Episode.query.all()]
    if episodes:
        return make_response(episodes, 200)
    else:
        return make_response({'Message': 'Error in accessing episodes'}, 404)

@episode_bp.route('/episodes/<int:id>', methods=['GET', 'DELETE'])
def episodes_by_id(id):
    if request.method == 'GET':
        episode = Episode.query.filter(Episode.id == id).first()
        if episode:
            return make_response(episode.to_dict(), 200)
        else:
            return make_response({'Message': 'Error in accessing episodes'}, 404)

    elif request.method == 'DELETE':
        episode = Episode.query.filter(Episode.id == id).first()
        db.session.delete(episode)
        db.session.commit()
        return make_response('', 204)