# FastAPI Mini Projects Learning Repository

This repository is now organized as a full learning journey, not just a set of course exercises.

It captures:
- Progressive FastAPI API design
- Validation and safer request handling
- SQLAlchemy integration with SQLite
- Auth with OAuth2 + JWT
- Role-based route protection
- Jinja templates + static files
- Alembic migration basics
- Test setup with dependency overrides

## Learning Path

1. `project1 Books CRUD Local`
- Core FastAPI routes
- Path/query params
- In-memory CRUD

2. `project2 Books CRUD Safer`
- Pydantic request models
- Field validation
- Better status codes and exceptions

3. `project3 Todos CRUD SQLite`
- DB models + sessions
- Routers by feature (`auth`, `todos`, `users`, `admin`)
- JWT auth, password hashing
- HTML templates and static assets
- Basic testing and migrations

## Documentation

- `docs/project-map.md`: What each project teaches and where to find it
- `docs/lessons-learned.md`: Practical lessons and pitfalls observed in this codebase
- `docs/fastapi-cheatsheet.md`: Commands, patterns, and quick references

## Quick Start

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run project 3:

```powershell
cd "project3 Todos CRUD SQLite"
uvicorn main:app --reload
```

Open:
- API docs: `http://127.0.0.1:8000/docs`
- Home page: `http://127.0.0.1:8000/`

## Notes

- Existing course project code is preserved.
- The new docs layer is meant to make revision faster and help turn this into a portfolio-ready study repo.

