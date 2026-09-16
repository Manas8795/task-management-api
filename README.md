# Task Management API

A lightweight RESTful Task Management API built with [FastAPI](https://fastapi.tiangolo.com/) and Python.

## 🚀 Features

- **Get all tasks**: Retrieve the entire list of tasks.
- **Get task by ID**: Retrieve details for a specific task.
- **Create task**: Add a new task with name and duration.
- **Update task**: Modify existing task fields.
- **Delete task**: Remove a task by ID.
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc docs.

## 📋 Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## 🛠️ Installation & Setup

1. **Clone the repository:**
   `ash
   git clone https://github.com/Manas8795/task-management-api.git
   cd task-management-api
   `

2. **Create and activate a virtual environment (optional but recommended):**
   `ash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   `

3. **Install dependencies:**
   `ash
   pip install -r requirements.txt
   `

4. **Run the API server:**
   `ash
   uvicorn main:app --reload
   `

5. **Access the API & Documentation:**
   - Interactive Swagger API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /get-task-all | Retrieve all tasks |
| GET | /get-task/{task_id} | Retrieve task by ID |
| POST | /post-task/{task_id} | Create a new task |
| PUT | /put-task/{task_id} | Update an existing task |
| DELETE | /del-task/{task_id} | Delete a task by ID |
