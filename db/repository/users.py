"""
User creation
"""
from sqlalchemy.orm import Session

from api.api_models.user import UserSignup
from db.models.user import User


def create_new_user(user: UserSignup, db: Session) -> User:

    new_user = user.model_dump().copy()
    new_user.pop("password_confirmation")

    new_user = User(**new_user)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
