from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuration for the app
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize migration
    login_manager.init_app(app)

    # Import and register routes
    from . import routes
    app.register_blueprint(routes.bp)

    # Set up login view (redirects unauthenticated users)
    login_manager.login_view = 'main.login'

    return app

# Delay the import of models to prevent circular import
@login_manager.user_loader
def load_user(user_id):
    from .models import User  # Import User only when needed
    return User.query.get(int(user_id))  # Fetch user from the database by ID
