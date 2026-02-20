# Secure Task API

A scalable REST API built using Django REST Framework with JWT authentication and role-based access.

---

## Features

- User Registration
- JWT Login Authentication
- Role-Based Access (User/Admin)
- Task CRUD APIs
- User-specific task filtering
- Pagination
- Swagger Documentation

---

## Tech Stack

- Django
- Django REST Framework
- SimpleJWT
- SQLite (can switch to PostgreSQL)

---

## API Endpoints

### Authentication
- POST /api/v1/register/
- POST /api/v1/login/
- POST /api/v1/refresh/

### Tasks
- GET /api/v1/tasks/
- POST /api/v1/tasks/
- PUT /api/v1/tasks/{id}/
- DELETE /api/v1/tasks/{id}/

---

## How to Run

```bash
git clone <repo-url>
cd secure-task-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Security Features

- Password hashing
- JWT token authentication
- Owner-based permissions
- Input validation
- Protected routes

---

## Scalability Notes

- Can integrate Redis for caching
- Can use PostgreSQL for production
- Can deploy using Docker
- Supports modular expansion

---

## Author

Nihal Kumar Singh
