#Alexander Shelton
#Holds the function that is called in run.py 

import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    #Importing blueprint instances
    from .main.routes import main
    #registering blueprints
    app.register_blueprint(main)

    return app
