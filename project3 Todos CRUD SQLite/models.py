# What kind of database tables will be created
from database import Base # we creating this model for database.py file
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class Users(Base):
    __tablename__ = "users" # name of the table in the database
    id = Column(
        Integer, 
        primary_key=True,
        index = True # indexable: unique
        )
    email = Column(
        String,
        unique=True
    )
    username = Column(
        String,
        unique=True
    )
    first_name = Column(
        String
    )
    last_name = Column(
        String
    )
    hashed_password = Column(
        String
    )
    is_active = Column(
        Boolean,
        default=True
    )
    role = Column(
        String
    )

class Todos(Base):
    __tablename__ = "todos" # name of the table in the database
    id = Column(
        Integer, 
        primary_key=True,
        index = True # indexable: unique
        )
    title = Column(
        String
    )
    description = Column(
        String
    )
    priority = Column(
        Integer
    )
    complete = Column(
        Boolean,
        default=False
    )   
    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )