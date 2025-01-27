from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # Import db directly from app, as it's initialized in __init__.py
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to link posts to users
    content = db.Column(db.Text, nullable=False)  # Example: Post content
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for the post

    def __repr__(self):
        return f'<Post {self.id} by User {self.user_id}>'

# Add relationship in User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)  # Relationship to access posts by user

    def __repr__(self):
        return f'<User {self.email}>'