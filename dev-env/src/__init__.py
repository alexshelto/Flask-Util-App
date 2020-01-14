#Alexander Shelton
#Holds the function that is called in run.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Configuration File: src/config.py
from src.config import Config



# #Creating db instance, called back in model.py
db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Configuring FlaskApp from config.py file. allows multiple instances
    db.init_app(app)

    # with app.app_context():
    #     db.create_all()



    #Importing blueprint instances
    from src.main.routes import main
    from src.data.routes import data

    #registering blueprints
    app.register_blueprint(main)
    app.register_blueprint(data)

    return app
