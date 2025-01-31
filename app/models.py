# app/models.py
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # Import db directly from app, as it's initialized in __init__.py
from datetime import datetime

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Editable fields for personal information
    name = db.Column(db.String(100), nullable=True)
    quote = db.Column(db.String(200), nullable=True)
    goal = db.Column(db.String(200), nullable=True)

    posts = db.relationship('Post', backref='author', lazy=True)  # Relationship to access posts by user

    def __repr__(self):
        return f'<User {self.email}>'

# Post Model (for reflections)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reflection = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Store the timestamp of the post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to link to the user

    def __repr__(self):
        return f'<Post {self.id} by User {self.user_id}>'
