import api.welcome.welcome_rest as welcome_rest_api


def init(app):
  # group routes
  app.register_blueprint(welcome_rest_api)
