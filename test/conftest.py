"""
Test configuration
"""
from typing import Any
# from fastapi import HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import pytest

from core.config import settings
from db.database import Base, get_db
from db.models.roles import Role
from utils.utils import RoleChoices
from app import app

pg_user = settings.POSTGRES_USER
pg_pass = settings.POSTGRES_PASSWORD
pg_host = settings.POSTGRES_SERVER
pg_port = settings.POSTGRES_PORT
pg_test_db = settings.POSTGRES_TEST_DB

TEST_SQLALCHEMY_DATABASE_URL = f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_test_db}"

engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


@pytest.fixture()
def session() -> Any:
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client(session: Session) -> Any:
    def override_get_db() -> Any:
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture(autouse=True)
def create_roles(session: Session) -> None:
    db: Session = session

    create_roles = [
        Role(name=RoleChoices.Admin),
        Role(name=RoleChoices.Student),
        Role(name=RoleChoices.Staff),
        Role(name=RoleChoices.Accountant),
        Role(name=RoleChoices.Parent),
        Role(name=RoleChoices.Headmaster),
        Role(name=RoleChoices.Proprietor)
    ]
    for role in create_roles:
        check_role = db.query(Role).filter(Role.name == role.name).first()
        if not check_role:
            db.add(role)

    db.commit()


@pytest.fixture
def test_user(client: Any) -> Any:
    user: dict[str, str] = {
        "first_name": "Fixtureuser",
        "last_name": "Emeka",
        "email": "fixtureuser@gmail.com",
        "password": "food1234",
        "password_confirmation": "food1234",
    }
    res = client.post("/api/v1/users/register/", json=user)

    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user.get("password")
    return new_user


# @pytest.fixture
# def mock_create_reset_token(mocker) -> Any:
#     return mocker.patch('api.routes.auth.create_reset_token', return_value="test_reset_token")


# @pytest.fixture
# def mock_send_email(mocker) -> Any:
#     return mocker.patch('utils.mail_service.send_email', return_value={"message": "Email has been sent"})
