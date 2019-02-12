from flask import Flask
from .main import views 





def create_app(config_name):
      app = Flask(__name__)




      return app