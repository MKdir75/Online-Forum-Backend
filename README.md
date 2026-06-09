# Online Forum Backend

A backend service for an online forum application built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, and **JWT authentication**.  
This project provides APIs for managing users, forums, posts, and comments with secure login.

---

## 🚀 Features
- User registration and JWT-based authentication
- Forum creation and listing
- Post and comment management
- Moderation tools
- PostgreSQL database integration

---

## 🛠️ Tech Stack
- **FastAPI** (Python web framework)
- **SQLAlchemy** (ORM)
- **PostgreSQL** (Database)
- **JWT (JSON Web Token)** for authentication
- **Uvicorn** (ASGI server)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/MKdir75/Online-Forum-Backend.git
cd Online-Forum-Backend

2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
DATABASE_URL=postgresql://username:password@localhost:5432/forumdb
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Run the server
uvicorn app.main:app --reload

📡 API Endpoints
POST /api/users/ → Register new user
POST /api/users/login → Login with JWT
GET /api/forum/ → List forums
POST /api/forum/ → Create new forum (JWT required)
GET /api/comments/ → List comments
POST /api/comments/ → Add comment (JWT required)
