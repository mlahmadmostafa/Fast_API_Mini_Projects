from fastapi import APIRouter


from typing import Annotated
from fastapi import Depends, HTTPException, Path
from models import Todos
from database import SessionLocal
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user
router = APIRouter(prefix="/todos", tags=["todos"])


# makes fastapi quicker as it fetches data then closes connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

# Field is for checkers
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

# Dependency injection we need to do something before executing what we need
# this function relies on our db opening up returning the result and then closes afterwards
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    return db.query(Todos).filter(Todos.owner_id == user.get("user_id")).all()

# no matter the outcome, status is 200 if no error happens
@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
def read_todo(db: db_dependency, todo_id: int = Path(gt=0),  user: user_dependency = None):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    # ID have one match as it is a primary key
    todo_model = db.query(Todos)\
        .filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get("user_id"))\
        .first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail="Not Found")


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get("user_id"))
    
    db.add(todo_model)
    db.commit()
    
# Update request method
@router.put("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    db: db_dependency,
    todo_request: TodoRequest,
    todo_id: int = Path(gt=0),
    user: user_dependency = None):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    todo_model = db.query(Todos)\
        .filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get("user_id"))\
        .first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    # Use the same todo model we retrieved from the database
    # SQL alchemy will know that this todo we are..
    # changing is the one we retrieved
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    
    # if we created a new one, it will confuse id creation
    # and it will think it is a new record, with an identical id
    # so it is either error or dupe
    
    db.add(todo_model)
    db.commit()

# All endpoints need to start with /
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(db: db_dependency, todo_id: int = Path(gt=0), user: user_dependency = None):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("user_id")).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found.")
    db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("user_id")).delete()
    db.commit()