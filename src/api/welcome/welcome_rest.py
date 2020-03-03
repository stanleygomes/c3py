from flask import Blueprint, escape, request

welcome_api = Blueprint('welcome_api', __name__, url_prefix='/welcome')


@welcome_api.route('/', methods=['GET'])
def index():
  # return redirect(url_for('dashboard')
  name = request.args.get('name', 'World')
  return f'Hello, {escape(name)}!'
