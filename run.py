from app import create_app

app = create_app()

if __name__ == "__main__":
    # Only use the Flask development server if running locally, not in production
    app.run(host='0.0.0.0', port=5000, debug=True)
