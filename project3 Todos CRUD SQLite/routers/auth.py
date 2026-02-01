from fastapi import APIRouter
from pydantic import BaseModel
from models import Users


class CreateUserRequest(BaseModel):
    username:str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str
    # ID is auto created
    # Every user is active by default
router = APIRouter()
@router.get("/auth/")
async def create_user(create_user_request: CreateUserRequest):
    user_model = Users.query(
        email = CreateUserRequest.
    )
    
    return {'user':'authenticated'}