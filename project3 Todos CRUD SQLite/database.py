from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'sqlite:///project3_app.db' # Database is local inside the project3 folder
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:z@localhost/TodoApplicationDatabase' # Database is local inside the project3 folder
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zzzz@localhost/TodoApplicationDatabase' # Database is local inside the project3 folder

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, 
    # connect_args={"check_same_thread": False} #SQLITE ONLY # It’s okay if this connection is shared across multiple threads.
)

try:
    with engine.connect() as connection:
        # We send a simple "ping" to the database
        connection.execute(text("SELECT 1"))
        print("🚀 Successfully connected to Database!")
except Exception as e:
    print("❌ Connection failed!")
    print(f"Error details: {e}")
    raise
SessionLocal = sessionmaker(
    autocommit=False, # We want to control when changes are committed to the database.
    autoflush=False, # We will manually flush changes to the database.
    bind=engine
    )

Base = declarative_base() # Base to control our database
