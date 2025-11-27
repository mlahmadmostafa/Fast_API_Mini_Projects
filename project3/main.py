from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Path
import models
from models import Todos
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
app = FastAPI()

# this craetes the database (or uses existing) on run
models.Base.metadata.create_all(bind = engine) 


# makes fastapi quicker as it fetches data then closes connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Field is for checkers
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

# Dependency injection we need to do something before executing what we need
# this function relies on our db opening up returning the result and then closes afterwards
@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()
# no matter the outcome, status is 200 if no error happens
@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    # ID have one match as it is a primary key
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail="Not Found")


@app.post('/todo', status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    
    db.add(todo_model)
    db.commit()
    
# Update request method
@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    db: db_dependency,
    todo_request: TodoRequest,
    todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
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