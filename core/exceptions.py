"""
Define the HTTP Exceptions to be raised
"""
# from typing import Any


class CustomException:
    USER_EXISTS: str = "User with the email already exists"
    PASSWORDS_MISMATCH: str = "Passwords do not match"
    USER_NOT_FOUND: str = "User with specified email does not exist"
    INVALID_PASSWORD: str = "Invalid password specified for the user"


exceptions = CustomException()
