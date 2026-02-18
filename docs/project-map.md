# Project Map

## Project 1: `project1 Books CRUD Local`

Primary file:
- `project1 Books CRUD Local/books.py`

Key topics:
- FastAPI app creation
- Basic CRUD endpoints
- Path and query parameters
- Route ordering (`/books/latest` before `/books/{book_id}`)
- Running with Uvicorn

What to improve next:
- Replace raw `dict` bodies with Pydantic models
- Use HTTPException and status codes consistently

## Project 2: `project2 Books CRUD Safer`

Primary file:
- `project2 Books CRUD Safer/books.py`

Key topics:
- `BaseModel` request schemas
- `Field()` validation constraints
- `Path` and `Query` parameter validation
- Use of `HTTPException`

What to improve next:
- Move from in-memory list to database persistence
- Fix type consistency in `search_books` (rating should be numeric end-to-end)

## Project 3: `project3 Todos CRUD SQLite`

Primary files:
- `project3 Todos CRUD SQLite/main.py`
- `project3 Todos CRUD SQLite/database.py`
- `project3 Todos CRUD SQLite/models.py`
- `project3 Todos CRUD SQLite/routers/auth.py`
- `project3 Todos CRUD SQLite/routers/todos.py`
- `project3 Todos CRUD SQLite/routers/users.py`
- `project3 Todos CRUD SQLite/routers/admin.py`

Key topics:
- SQLAlchemy engine/session setup
- Relational models (`Users`, `Todos`)
- Modular router architecture
- Auth flow:
  - register user
  - login via OAuth2 form
  - issue JWT token
  - protect routes with dependency injection
- Role-based admin routes
- Jinja2 templates and static file mounting
- Test isolation with dependency overrides

Migration and test helpers:
- `alembic_commands.ps1`
- `project3 Todos CRUD SQLite/alembic/...`
- `project3 Todos CRUD SQLite/tests/test_db.py`
- `pytest.md`

