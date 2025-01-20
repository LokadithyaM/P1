from flask import Flask
from .models import db  # Import the db object
from .routes import bp  # Import your blueprint

def create_app():
    app = Flask(__name__)

    # Configuration (Make sure this is present)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # SQLite for local development
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
    app.secret_key = 'your_secret_key'

    db.init_app(app)  # Initialize the database with the app

    # Register blueprint
    app.register_blueprint(bp)

    return app
