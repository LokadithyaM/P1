from flask import Blueprint, render_template

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

@bp.route('/signup')
def signup():
    return render_template('signup.html')  # Render the signup page

