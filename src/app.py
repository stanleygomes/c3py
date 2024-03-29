# -*- coding: utf-8 -*-

import os
from flask_cors import CORS
from flask import Flask, g
from dotenv import load_dotenv

import utils.config as config
import routes.routes as routes

if __name__ == "__main__":
  load_dotenv()

  # flask instance
  app = Flask(__name__)
  CORS(app)

  # app routes
  routes.init(app)

  # app config
  http_host = config.http_host()
  http_port = config.http_port()
  debug = config.log_debug()

  # run app
  app.run(host=http_host, port=http_port, debug=debug)
