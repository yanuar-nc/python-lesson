from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

app = Flask(__name__)
api = Api(app)


app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

import routes # include all routes from routes.py

if __name__ == '__main__':
    app.run()