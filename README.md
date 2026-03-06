# Task Tracker API

A modern, fully asynchronous RESTful API for task management, built with FastAPI. 
This project serves as a robust backend foundation, demonstrating modern Python development practices, relational database design, and containerization.

## Tech Stack
* **Framework:** FastAPI
* **Language:** Python 3.11+
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy 2.0 (Async)
* **Migrations:** Alembic
* **Authentication:** JWT (JSON Web Tokens) & PassLib (Bcrypt)
* **Testing:** Pytest & HTTPX
* **Containerization:** Docker & Docker Compose

## Key Features
* **User Authentication:** Secure registration and login using JWT. Passwords are cryptographically hashed.
* **CRUD Operations:** Complete lifecycle management for tasks (Create, Read, Update, Delete).
* **Relational Data:** One-to-Many relationships established between `Categories` and `Tasks`.
* **Advanced Querying:** The `GET /tasks/` endpoint supports pagination (`limit`, `skip`) and filtering (`is_completed`, `category_id`).
* **Background Tasks:** Asynchronous background processes (e.g., simulating welcome email delivery upon user registration) to ensure fast API response times.
* **Automated Testing:** Integration tests built with Pytest to ensure API reliability.

## Quick Start (Docker)

The easiest way to run this project is using Docker. You don't need to install Python or PostgreSQL on your local machine.

1. Clone the repository:
   ```bash
   git clone [https://github.com/YaroslavMilchenko/task_tracker_project]
   cd task_tracker_project

2. Start the application and database containers:
    docker-compose up -d --build

3. Access the interactive API documentation (Swagger UI) at:
    http://localhost:8000/docs

## To run the automated tests locally:
    pytest