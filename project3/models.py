# What kind of database tables will be created
from database import Base # we creating this model for database.py file
from sqlalchemy import Column, Integer, String, Boolean
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