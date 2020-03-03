from flask import Blueprint, jsonify, request, abort

welcome_api = Blueprint('welcome_api', 'welcome_api', url_prefix='/welcome')


@welcome_api.route('/', methods=['GET'])
def index():
  return 'hello world!'
