from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy
from .models import User, Note
from os import path

# Database initialization
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key111'
    app.config['SQLAlchemy_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    return app

# Check if database exists
# If not create it
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created Database.")