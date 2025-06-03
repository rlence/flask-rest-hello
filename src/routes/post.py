from flask import Flask, request, jsonify, url_for, Blueprint

api = Blueprint('api/post', __name__)


@api.route('/', methods=['GET'])
def get_posts():

    return jsonify('get post'), 200
