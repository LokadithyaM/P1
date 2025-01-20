from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database URI configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Or use your preferred database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional but recommended

    # Initialize the app with the SQLAlchemy instance
    db.init_app(app)

    return app
