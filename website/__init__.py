from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy

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

    return app