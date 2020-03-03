from flask import Blueprint, jsonify, request, abort

welcome_rest_api = Blueprint('welcome_rest_api', 'welcome_rest_api', url_prefix='/welcome')


@welcome_rest_api.route('/', methods=['GET'])
def index():
  return 'hello world!'
