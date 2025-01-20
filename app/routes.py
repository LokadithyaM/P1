from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, User  # Ensure to import your db and User model

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/login')
def login():
    return render_template('login.html')  # Render the login page

@bp.route('/signup', methods=['GET', 'POST'])  # Add POST method here
def signup():
    if request.method == 'POST':  # Check if it's a POST request
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the passwords match
        if password != confirm_password:
            flash("Passwords don't match. Please try again.", 'error')
            return redirect(url_for('main.signup'))

        # Check if the email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please log in.', 'error')
            return redirect(url_for('main.signup'))

        # Create a new user if email is not already registered
        new_user = User(email=email)
        new_user.set_password(password)  # Hash the password before storing it
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('main.login'))  # Redirect to the login page after signup

    return render_template('signup.html')  # Render the signup page if GET request

