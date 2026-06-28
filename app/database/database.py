import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine():
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise Exception("DATABASE_URL not found in environment")
    return create_engine(database_url, pool_pre_ping=True)

engine = get_engine()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()