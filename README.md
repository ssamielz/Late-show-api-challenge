## Late Show API Challenge
A Flask REST API for managing guests and episodes of a Late Night TV show.

📁 Folder Structure
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── tests/
├── challenge-4-lateshow.postman_collection.json
└── README.md

⚙️ Setup Instructions
1. Clone and install dependencies
late-show-api-challenge.git
cd late-show-api-challenge
pipenv install
pipenv shell
2. Create the PostgreSQL database
CREATE DATABASE late_show_db;
3. Configure server/config.py
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "your-secret-key"
4. Run migrations and seed data
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial"
flask db upgrade
python server/seed.py

🔐 Authentication Flow
Register
POST /register
{
  "username": "john",
  "password": "doe123"
}
Login
POST /login
{
  "username": "john",
  "password": "doe123"
}
Response:

{
  "access_token": "..."
}
Use the token for protected routes:

Authorization: Bearer <access_token>

🚀 API Routes
Method	Endpoint	Auth Required?	Description
POST	/register	❌	Register a new user
POST	/login	❌	Login and receive a JWT token
GET	/episodes	❌	List all episodes
GET	/episodes/int:id	❌	Get an episode and its appearances
DELETE	/episodes/int:id	✅	Delete an episode and appearances
GET	/guests	❌	List all guests
POST	/appearance	✅	Create a new appearance

🧪 Testing
Run tests with Pytest
pytest
Auth routes tested (/register, /login)
Uses in-memory SQLite for test isolation

📬 Postman
Import challenge-4-lateshow.postman_collection.json into Postman.

Includes Register, Login, Protected routes
Easily test with valid JWT tokens
