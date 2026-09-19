# Task Management API

A robust RESTful Task Management API built with [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy ORM](https://www.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/), and [Pydantic v2](https://docs.pydantic.dev/).

## 🚀 Features

- **Database Persistence**: Fully integrated with PostgreSQL via SQLAlchemy ORM.
- **Data Validation & Serialization**: Pydantic schemas for request validation (`TaskCreate`, `TaskUpdate`) and responses (`TaskResponse`).
- **FastAPI Dependency Injection**: Clean database session lifecycle management with `Depends(get_db)`.
- **CRUD Operations**: Complete Create, Read, Update, and Delete endpoints for task management.
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc docs.

## 📋 Requirements

- Python 3.8+
- PostgreSQL
- Dependencies listed in `requirements.txt` (`fastapi`, `uvicorn`, `sqlalchemy`, `psycopg[binary]`, `python-dotenv`)

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Manas8795/task-management-api.git
   cd task-management-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory (refer to `.env.example`):
   ```env
   DATABASE_URL=postgresql+psycopg://<username>:<password>@localhost:5432/<database_name>
   ```

5. **Run the API server:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API & Documentation:**
   - Interactive Swagger API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 API Endpoints

| Method | Endpoint | Description | Request Body | Response |
|---|---|---|---|---|
| `GET` | `/get-task-all` | Retrieve all tasks | None | `List[TaskResponse]` |
| `GET` | `/get-task/{task_id}` | Retrieve task by ID | None | `TaskResponse` |
| `POST` | `/post-task` | Create a new task | `TaskCreate` | `TaskResponse` |
| `PUT` | `/put-task/{task_id}` | Update an existing task | `TaskUpdate` | `TaskResponse` |
| `DELETE` | `/del-task/{task_id}` | Delete a task by ID | None | `{"Msg": "Task deleted successfully"}` |

## 🏗️ Project Architecture

```
task-management-api/
├── database.py       # Database engine, SessionLocal, and get_db dependency
├── models.py         # SQLAlchemy ORM database models
├── schemas.py        # Pydantic validation and serialization models
├── main.py           # FastAPI routes and application entrypoint
├── requirements.txt  # Project dependencies
├── .env.example      # Example environment variables template
├── .gitignore        # Git ignore rules (protects .env and caches)
└── README.md         # Project documentation
```
