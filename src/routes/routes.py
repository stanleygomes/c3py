import api.welcome.welcome_rest as welcome_rest


def init(app):
  # group routes
  app.register_blueprint(welcome_rest)

  @app.errorhandler(404)
  def not_found(error):
    return {'error': True, 'message': 'Pagina nao encontrada'}

  @app.errorhandler(400)
  def bad_request():
    return {'error': True, 'message': 'Erro de requisicao'}

  @app.errorhandler(500)
  def server_error():
    return {'error': True, 'message': 'Erro interno de servidor'}
