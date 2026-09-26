from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Explicitly load single root .env file
root_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
if os.path.exists(root_env_path):
    load_dotenv(root_env_path)
else:
    load_dotenv()


default_db = "sqlite:///./agentgrid.db"
if not os.getenv("DATABASE_URL"):
    if os.path.exists(os.path.join(os.path.dirname(__file__), "agentgrid.db")):
        default_db = "sqlite:///./agentgrid.db"
    elif os.path.exists(os.path.join(os.path.dirname(__file__), "founderos.db")):
        default_db = "sqlite:///./founderos.db"

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", default_db)

connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
