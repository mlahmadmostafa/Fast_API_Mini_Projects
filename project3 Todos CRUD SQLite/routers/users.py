from fastapi import APIRouter


from typing import Annotated
from fastapi import Depends, HTTPException, Path
from models import Users
from database import SessionLocal
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

router = APIRouter(prefix="/users", tags=["users"])

# makes fastapi quicker as it fetches data then closes connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=["argon2"], deprecated="auto")


@router.post("/get_user", status_code=status.HTTP_200_OK)
async def get_user_info(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    user_model = db.query(Users).filter(Users.id == user.get("user_id")).first()
    return user_model

@router.post("/change_password")
async def change_user_password(db: db_dependency, user: user_dependency, old_password: str, new_password: str):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    user_model = db.query(Users).filter(Users.id == user.get("user_id")).first()
    if bcrypt_context.verify(old_password, user_model.hashed_password):
        user_model.hashed_password = bcrypt_context.hash(new_password)
        db.commit()
    else:
        raise HTTPException(status_code=401, detail="Not authenticated")