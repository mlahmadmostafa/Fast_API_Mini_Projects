from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABASE_URI = 'sqlite:///project3_app.db' # Database is local inside the project3 folder



engine = create_engine(
    SQLALCHEMY_DATABASE_URI, 
    connect_args={"check_same_thread": False} # It’s okay if this connection is shared across multiple threads.
)
SessionLocal = sessionmaker(
    autocommit=False, # We want to control when changes are committed to the database.
    autoflush=False, # We will manually flush changes to the database.
    bind=engine
    )

Base = declarative_base() # Base to control our database
