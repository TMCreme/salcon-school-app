"""
OAuth 2 Authentication
"""
from jose import jwt, JWTError
from datetime import datetime, timedelta
import re
from api.api_models.user import TokenData
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from sqlalchemy.orm import Session

from db import database
from db.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


credential_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET, algorithm=settings.ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.REFRESH_SECRET, algorithm=settings.ALGORITHM)
    return token


def get_access_token(sub: str):
    token = create_access_token({"sub": sub})
    return token


def get_refresh_token(sub: str):
    token = create_refresh_token({"sub": sub})
    return token


def verify_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, settings.SECRET, algorithms=settings.ALGORITHM)
        sub = payload.get('sub')
        if sub is None:
            raise credential_exception
        token_data = TokenData(id=sub)
    except JWTError:
        raise credential_exception

    return token_data


def verify_refresh_token(token: str):
    payload = jwt.decode(token, settings.REFRESH_SECRET, algorithms=settings.ALGORITHM)
    sub = payload.get('sub')
    if sub is None:
        return False
    return TokenData(id=sub)


# Get currently logged in User
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(database.get_db)):

    token = verify_token(token, credential_exception)
    user = db.query(User).filter(User.id == token.id).first()
    if not user:
        raise credential_exception
    if not user.is_active:
        raise HTTPException(status_code=302, headers={"Location": "/inactive"})
    return user


def create_reset_token(email: str) -> str:
    delta = timedelta(minutes=15)
    now = datetime.utcnow()
    payload = {
        "sub": email,
        "iat": now,
        "exp": now + delta
    }
    return jwt.encode(payload, settings.SECRET, algorithm=settings.ALGORITHM)


def verify_reset_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.SECRET, algorithms=settings.ALGORITHM)
        email = payload.get("sub")
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise HTTPException(status_code=400, detail="Invalid token")
        expiration = payload.get("exp")
        if expiration:
            expiration_datetime = datetime.utcfromtimestamp(expiration)
            if datetime.now() > expiration_datetime:
                raise HTTPException(status_code=400, detail="Token has expired")
        return email
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")
