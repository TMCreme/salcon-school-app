"""
Authentication and Authorization APIs
"""
from typing import Any
from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.api_models.user import UserResponse, UserSignup, Token
from db.database import get_db
from db.models.user import User
from db.repository.users import create_new_user
from core.exceptions import exceptions
from utils.oauth2 import get_access_token, get_refresh_token
from utils.utils import get_password_hash, verify_password


auth_router = APIRouter(tags=["Auth"], prefix="/users")

oath2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@auth_router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def signup(user: UserSignup, db: Session = Depends(get_db)) -> Any:
    """Signup endpoint for the user model"""
    user_email = user.email.lower()
    _user_email_query = db.query(User).filter(User.email == user_email).first()
    if _user_email_query:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=exceptions.USER_EXISTS
        )
    hash_passwd = get_password_hash(user.password)

    if user.password != user.password_confirmation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=exceptions.PASSWORDS_MISMATCH
        )
    user.password = hash_passwd
    new_user: Any = create_new_user(user, db)
    return new_user


@auth_router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Any:
    """Login with OAuth2 Passowrd Form"""
    user_email = user.username.lower()
    user_data = db.query(User).filter(User.email == user_email).first()
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=exceptions.USER_NOT_FOUND
        )

    if not verify_password(user.password, user_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=exceptions.INVALID_PASSWORD
        )

    token = get_access_token(str(user_data.id))
    refresh_token = get_refresh_token(str(user_data.id))

    return Token(
        token=token,
        refresh_token=refresh_token,
        token_type="Bearer",
        is_active=user_data.is_active
    )


@auth_router.post("/logout")
def logout(response: Response):
    response.set_cookie(key="st.token", value="", httponly=True, max_age=10, samesite="none", secure=True)
    return {"message": "Logout Successful"}
