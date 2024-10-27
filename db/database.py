"""
Database settings for the SQLAchemy ORM
"""
from typing import Any
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings


pg_user: str = settings.POSTGRES_USER
pg_pass: str = settings.POSTGRES_PASSWORD
pg_server: str = settings.POSTGRES_SERVER
pg_port: int = settings.POSTGRES_PORT
pg_db: str = settings.POSTGRES_DB

SQLALCHEMY_DB_URL = f"postgresql://{pg_user}:{pg_pass}@{pg_server}:{pg_port}/{pg_db}"


def set_up_db(production_env) -> tuple[Any, Any, Any]:
    """Setting up the env specific db"""
    if production_env:
        engine: Engine = create_engine(settings.DATABASE_URL)
    else:
        engine: Engine = create_engine(SQLALCHEMY_DB_URL)
    SessionLocal: Any = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    return engine, SessionLocal, Base


engine, SessionLocal, Base = set_up_db(settings.PRODUCTION_ENV)


def get_db() -> Any:
    db: Any = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def create_
