"""
Serializer for the user model
"""
from typing import Optional, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator, EmailStr
from utils.utils import RoleChoices


class Role(BaseModel):
    id: int = Field(...)
    name: str = Field(...)

    model_config = ConfigDict(from_attributes=True)


class UserSignup(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
    password_confirmation: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    role_id: Optional[int] = Field(None)

    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    @field_validator("role_id", mode="before", check_fields=True)
    def set_role_id(cls, role_id) -> Any:
        from db.database import SessionLocal
        from db.models.roles import Role as _Role
        db = SessionLocal()
        check_role = db.query(_Role).filter(
            _Role.name == RoleChoices.Student).first()
        db.close()
        if not check_role:
            return role_id
        return role_id or check_role.id


class UserResponse(BaseModel):
    id: int = Field(...)
    email: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    is_active: bool = Field(...)
    role: Optional[Role] = Field(None)


class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class Token(BaseModel):
    token: str = Field(...)
    token_type: str = Field(...)
    is_active: bool = Field(...)
    refresh_token: str = Field(...)


class TokenData(BaseModel):
    id: Optional[str] = Field(default=None)


class RefreshTokenRequest(BaseModel):
    refresh_token: str = Field(...)


class ForgotPasswordRequest(BaseModel):
    email: EmailStr = Field(...)


class ResetPasswordRequest(BaseModel):
    token: str = Field(...)
    new_password: str = Field(...)
