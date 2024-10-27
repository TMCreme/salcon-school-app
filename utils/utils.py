"""
Helper functions and others
"""
import os
from typing import Any
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password) -> Any:
    return pwd_context.hash(password)


def verify_password(plain_password, password) -> Any:
    return pwd_context.verify(plain_password, password)


def is_image_file(file_name) -> bool:
    image_formats = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico'}
    _, file_extension = os.path.splitext(file_name)

    return file_extension.lower() in image_formats


class RoleChoices():
    Admin: str = "Admin"
    Accountant: str = "Accountant"
    Parent: str = "Parent"
    Student: str = "Student"
    Staff: str = "Staff"
    Headmaster: str = "Headmaster"
    Proprietor: str = "Proprietor"
