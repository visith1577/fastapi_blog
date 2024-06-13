from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_URL = "sqlite:///./blog_api.db"

engine = create_engine(SQLALCHEMY_URL, connect_args={"check_same_thread": False})

session_local = sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
