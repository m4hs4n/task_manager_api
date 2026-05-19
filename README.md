# Task Manager API 📝

A simple REST API for managing tasks — built entirely from scratch with FastAPI, without following any tutorial.

🚀 **Live API Docs:** coming soon

---

## What it does

- Create tasks with title, description and duration
- View all tasks
- Update any task field
- Delete tasks by ID
- Input validation with Pydantic

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Validation | Pydantic |
| Server | Uvicorn |
| Storage | In-memory (list) |

---

## Project Structure

```
task_manager_api/
├── app/
│   ├── app.py        # FastAPI routes
│   └── schemas.py    # Pydantic models
└── main.py           # Entry point
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/m4hs4n/task_manager_api.git
cd task_manager_api
```

### 2. Set up the environment

```bash
uv venv
uv pip install fastapi uvicorn
```

### 3. Run it

```bash
uv run main.py
```

API available at `http://localhost:8000`  
Swagger docs at `http://localhost:8000/docs`

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

## Task Model

```json
{
  "id": "uuid",
  "title": "Study FastAPI",
  "description": "Read the docs",
  "duration_min": 60,
  "done": false
}
```

---

## What I Learned

- Building a REST API from scratch without a tutorial
- Pydantic models for input validation and response schemas
- CRUD operations with proper HTTP status codes and error handling
- FastAPI route decorators and path parameters
