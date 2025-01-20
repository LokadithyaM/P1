from app import create_app
from app.models import db  # Import the db from models

app = create_app()

# This will create the tables in the database
with app.app_context():
    db.create_all()  # Create all tables (this is required the first time you run the app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # This will run the Flask app in development mode
