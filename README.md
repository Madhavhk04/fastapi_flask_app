# FastAPI + Flask Full-Stack Boilerplate

A modern, production-ready full-stack web application featuring a **FastAPI** backend, a **PostgreSQL** database, and a **Flask** frontend styled with a stunning **Glassmorphism** aesthetic.

## 🚀 Features
- **FastAPI Backend (Python):** High-performance API routing and logic.
- **Flask Frontend (Python):** Jinja templating and session management.
- **PostgreSQL Database:** Sturdy relational database via SQLAlchemy.
- **Secure Authentication:** JSON Web Token (JWT) architecture with bcrypt password hashing.
- **Full CRUD Capabilities:** Dynamic endpoints to Create, Read, Update, and Delete user profiles.
- **Premium Glassmorphism UI:** Frosted glass containers, ambient gradients, and fully responsive layout.

## 📁 Project Structure
```bash
fastapi_flask_app/
├── backend/
│   ├── main.py              # FastAPI endpoints and logic
│   ├── models.py            # SQLAlchemy database schemas
│   ├── database.py          # PostgreSQL connection setup
│   └── requirements.txt     # Backend dependencies
└── frontend/
    ├── app.py               # Flask application & routing
    ├── templates/           # Jinja HTML components (Glassmorphism UI)
    └── requirements.txt     # Frontend dependencies
```

## 🛠️ Getting Started

### 1. Prerequisites
- Python 3.9+
- PostgreSQL Server (Local or Cloud)

### 2. Setup the Environment
Clone the repository and optionally create a virtual environment in the root directory:
```bash
git clone https://github.com/Madhavhk04/fastapi_flask_app.git
cd fastapi_flask_app

python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Start the Backend API (Terminal 1)
```bash
# Navigate to the backend folder
cd backend

# Install dependencies
pip install -r requirements.txt

# Set your PostgreSQL URL (Make sure to encode special characters in the password!)
# Windows PowerShell:
$env:DATABASE_URL="postgresql://username:password@localhost:5432/yourdbname"
# Mac/Linux:
export DATABASE_URL="postgresql://username:password@localhost:5432/yourdbname"

# Start the server
uvicorn main:app --reload
```
*The FastAPI backend will automatically generate the required database tables and start running on `http://127.0.0.1:8000`.*

### 4. Start the Frontend App (Terminal 2)
Open a new terminal, activate your virtual environment, and run:
```bash
# Navigate to the frontend folder
cd frontend

# Install dependencies
pip install -r requirements.txt

# Start the Flask development server
python app.py
```

### 5. Access the Platform
Visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser!

## 🔐 Authentication Details
- Registration securely hashes passwords using `bcrypt` before database insertion.
- Login validates credentials and generates an encrypted JWT session token.
- Flask securely stores the JWT in its built-in session state and attaches it algorithmically to headers for protected FastAPI calls.
