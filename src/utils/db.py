from flask_sqlalchemy import SQLAlchemy
import config


def config_db(app):
  # TODO - get database params from dotenv file (config)
  print("URI: %s" % (db_uri))
  app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db = app.db = SQLAlchemy(app)

  return db
