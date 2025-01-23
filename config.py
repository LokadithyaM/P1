class Config:
    SECRET_KEY = 'mysecretkey'  # Change this to a secure key in production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Your database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Flask-Login related config (optional)
    LOGIN_DISABLED = False
