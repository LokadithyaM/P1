from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the database
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email field
    password = db.Column(db.String(200), nullable=False)  # Field for storing hashed password

    def __repr__(self):
        return f'<User {self.email}>'

    # Hash the password before saving it
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Check if the provided password matches the hashed password
    def check_password(self, password):
        return check_password_hash(self.password, password)
