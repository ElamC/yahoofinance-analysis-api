from flask import Blueprint, jsonify, request

blueprint = Blueprint('exceptions', __name__)

@blueprint.app_errorhandler(429)
def too_many_requests(e):
    return jsonify({'message': {e.name: {'desc': 'one request/sec allowed'}}, 'status_code': e.code, 'source': request.base_url})

@blueprint.app_errorhandler(404)
def not_found(e):
    return jsonify({'message': {e.name: {'desc': 'Symbol not found, please check your spelling and try again.'}}, 'status_code': e.code})
