from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # Import db directly from app, as it's initialized in __init__.py

class User(db.Model, UserMixin):  # Add UserMixin for Flask-Login compatibility
    id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # To store hashed password

    def __repr__(self):
        return f'<User {self.email}>'
    
    # Hash password before storing it
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Check password against stored hash
    def check_password(self, password):
        return check_password_hash(self.password, password)
