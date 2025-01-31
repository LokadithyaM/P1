from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User, Post
from flask_login import login_user,current_user

bp = Blueprint('main', __name__)

# Home route
@bp.route('/')
def index():
    return render_template('index.html')

# About route
@bp.route('/about')
def about():
    return render_template('about.html')

# Login route
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if the user exists in the database
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            # If the user exists and the password matches
            login_user(user)  # Log in the user using Flask-Login
            
            flash('Login successful!', 'success')
            return redirect(url_for('main.personal'))  # Redirect to home page

        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('main.login'))  # Redirect back to login page
    
    return render_template('login.html')

@bp.route('/personal.html', methods=['GET', 'POST'])
def personal():
    if request.method == 'POST':
        # Get the form data
        name = request.form.get('name')
        quote = request.form.get('quote')
        goal = request.form.get('goal')
        reflection = request.form.get('reflection')

        # Get the current logged-in user
        user = current_user  # current_user comes from Flask-Login

        if user:
            # Update the user's information (name, quote, goal)
            user.name = name
            user.quote = quote
            user.goal = goal

             # Create a new post for the reflection
            if reflection:
                new_post = Post(reflection=reflection, user_id=user.id)
                db.session.add(new_post)

            # Commit the changes to the database
            db.session.commit()

            # Clear reflection input for the form
            
            # Debugging the captured values
            print(f"Updated Name: {name}")
            print(f"Updated Quote: {quote}")
            print(f"Updated Goal: {goal}")
            print(f"Created Reflection: {reflection}")
            reflection = ""


            return redirect(url_for('main.personal'))  # Redirect to avoid re-posting the data

    # Render the user's current info and all their posts (reflections)
    user = current_user
    return render_template('personal.html', user=user)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #username = request.form.get('username') or 'default_user'
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
            return redirect(url_for('main.signup'))
        
        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User already exists. Please log in!', 'danger')
            return redirect(url_for('main.login'))
        
        # Hash the password (use the default method)
        hashed_password = generate_password_hash(password)
        
        # Create the new user
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Sign Up successful! Please log in.', 'success')
        return redirect(url_for('main.login'))  # Redirect to login page after signup
    
    return render_template('signup.html')


