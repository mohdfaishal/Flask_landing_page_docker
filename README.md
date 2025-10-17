📘 README.md
# Flask + PostgreSQL + Adminer (Docker Setup)

A simple Flask web application using PostgreSQL as the database and Adminer as a lightweight database management tool — all running in Docker containers.

---

## 🧱 Project Structure

flask-postgres-app/
│
├── app.py # Main Flask app
├── models.py # SQLAlchemy models
├── requirements.txt # Python dependencies
├── Dockerfile # Flask container setup
├── docker-compose.yml # Multi-container setup
├── .env # Environment variables (not committed)
├── .gitignore # Files to ignore in Git
│
├── static/ # Static assets (CSS, JS, images)
└── templates/ # HTML templates

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Build and Run with Docker
docker compose up --build

3️⃣ Access the Services
Service	URL	Description
Flask App	http://localhost:5000
	Main web app
Adminer	http://localhost:8080
	DB interface
PostgreSQL	localhost:5432	Database service
🗃️ Database Details
Variable	Value
DB Name	flaskdb
User	postgres
Password	postgres
Host	db
Port	5432

These are configured in your docker-compose.yml and Flask app environment.

🧩 Example API Endpoints
Method	Endpoint	Description
GET	/add/<name>	Add new user
DELETE	/delete/<name>	Delete user by name
GET	/users	List all users (optional)
🧰 Adminer Login

Visit http://localhost:8080

Select PostgreSQL

Use:

System: PostgreSQL
Server: db
Username: postgres
Password: postgres
Database: flaskdb

🧼 Common Docker Commands
# Stop containers
docker compose down

# Rebuild containers
docker compose up --build

# View logs
docker compose logs -f flask

🧑‍💻 Local Development (Optional)

If you want to run Flask locally (without Docker):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py


Then visit:
👉 http://127.0.0.1:5000
