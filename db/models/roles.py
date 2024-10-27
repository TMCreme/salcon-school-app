"""
Database models for User Roles
"""
from typing import Any
from sqlalchemy.orm.relationships import _RelationshipDeclared
from db.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from db.models.user import User


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    users: _RelationshipDeclared[Any] = relationship("User", order_by=User.id, back_populates="roles")
