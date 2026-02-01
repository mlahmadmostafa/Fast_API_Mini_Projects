from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos
app = FastAPI()

# this craetes the database (or uses existing) on run
models.Base.metadata.create_all(bind = engine) 

app.include_router(auth.router)
app.include_router(todos.router)
