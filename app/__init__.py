from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()


def create_app(config_name):
  app = Flask(__name__)

  #creating the app config
  app.config.from_object(config_options[config_name])


  #initialization of flask extentions
  bootstrap.init_app(app)

  #registering blueprint
  from.main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  #setting config
  # from .request import config_request
  # config_request(app)

  #add forms and views
  return app