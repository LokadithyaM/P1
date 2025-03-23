Itter

Itter is a multipurpose platform designed to help users record their progress, share thoughts, capture moments, and accomplish goals. It combines real-time interaction with goal tracking and AI-driven insights.

Features

User Authentication

Sign-in/Sign-up functionality

Independent user sessions

Secure password management

Goal Tracking & Management

Add/remove goals

Update progress status

Daily progress recording

Reflections & Insights

Store and view past reflections

AI-generated insights (Gemini integration - upcoming)

Real-time Communication

WebSockets for live updates

Heatmap.js for visual engagement tracking (planned)

Tech Stack

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Database: PostgreSQL / SQLite

Hosting: Railway / GitHub Pages

Real-Time: WebSockets

AI Integration: Gemini API (future increment)

Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/itter.git
cd itter

Create a virtual environment & install dependencies:

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Run the Flask application:

flask run

Access the app in your browser:

http://127.0.0.1:5000/

Deployment

The app is hosted on Railway and can be deployed by pushing changes to the repository. For production:

git push origin main

Upcoming Features

Heatmap.js for user activity visualization

Logout functionality

Enhanced past reflections with detailed views

AI-powered personalized insights

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.

License

MIT License

Author: Lokadithya MStatus: migrated to http://github.com/LokadithyaM/Awake
