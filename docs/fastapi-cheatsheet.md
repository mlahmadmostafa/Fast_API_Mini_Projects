# FastAPI Cheatsheet

## Run Commands

Project 1:
```powershell
cd "project1 Books CRUD Local"
uvicorn books:app --reload
```

Project 2:
```powershell
cd "project2 Books CRUD Safer"
uvicorn books:app --reload --host 127.0.0.1 --port 8080
```

Project 3:
```powershell
cd "project3 Todos CRUD SQLite"
uvicorn main:app --reload
```

## Common FastAPI Patterns

- Query/path validation:
```python
from fastapi import Path, Query
book_id: int = Path(gt=0)
rating: int = Query(ge=1, le=5)
```

- Request schema:
```python
from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
```

- HTTP errors:
```python
from fastapi import HTTPException
raise HTTPException(status_code=404, detail="Not found")
```

## Auth Flow (Project 3)

1. Register via `POST /auth/`
2. Login via `POST /auth/token` with OAuth2 form
3. Receive bearer token
4. Call protected routes with:
   - `Authorization: Bearer <token>`

## Testing

From project 3 folder:
```powershell
pytest -q
```

Key idea:
- Override dependencies (`get_db`, `get_current_user`) for isolated endpoint tests.

## Alembic Basics

Initialize (once):
```powershell
alembic init alembic
```

Create migration:
```powershell
alembic revision -m "describe change" --autogenerate
```

Apply migration:
```powershell
alembic upgrade head
```

Rollback one step:
```powershell
alembic downgrade -1
```

