"""
User model
"""
from sqlalchemy import Boolean, Column, String, Integer, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__: str = "users"
    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    last_modified = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'),
        server_onupdate=text('now()')
        )
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    password = Column(String, nullable=False)

    roles = relationship("Role",  back_populates="users")
