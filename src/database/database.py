from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# In a real application, get this from environment variables
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/project_manager_db"

enfine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=enfine)

Base = declarative_base()

