from flask import Flask, request, jsonify, url_for, Blueprint


api = Blueprint('api/user', __name__)


@api.route('/', methods=['GET'])
def get_users():

    return jsonify('get user'), 200
