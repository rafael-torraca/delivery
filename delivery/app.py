from flask import Flask
from delivery.ext import site
#from delivery.ext import admin



def create_app():
    app = Flask(__name__)
    site.init_app(app)
    #admin.init_app(app)
    return app