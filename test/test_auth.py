"""
Testing authentication APIs
"""
from typing import Any
# from datetime import datetime, timedelta
# import pytest
# from fastapi import HTTPException
from fastapi.testclient import TestClient
from app import app
from core.exceptions import exceptions
# from utils.mail_service import send_email
# from utils.oauth2 import create_reset_token, verify_reset_token


client = TestClient(app)

user_signup_payload: dict[str, str] = {
    "first_name": "Festus",
    "last_name": "Erasmus",
    "email": "tester123@email.com",
    "password": "Test1234",
    "password_confirmation": "Test1234"
}

user_signup_payload_incomplete: dict[str, str] = {
    "first_name": "Festus",
    "email": "tester123@email.com",
    "password": "Test1234"
}


def test_user_signup_valid(client: Any) -> None:
    res = client.post("/api/v1/users/register", json=user_signup_payload)
    res_body = res.json()

    assert res_body["email"] == user_signup_payload["email"]
    assert res.status_code == 201


def test_user_signup_invalid() -> None:
    res = client.post("/api/v1/users/register", json=user_signup_payload_incomplete)
    assert res.status_code == 422


def test_user_signup_invalid_confirm_password() -> None:
    payload = user_signup_payload.copy()
    payload["password_confirmation"] = "Test1235"
    res = client.post("/api/v1/users/register", json=payload)
    res_body = res.json()

    assert res.status_code == 400
    assert res_body["detail"] == exceptions.PASSWORDS_MISMATCH


def test_user_login_valid(test_user) -> None:
    res = client.post("/api/v1/users/login", data={
        "username": test_user.get("email"),
        "password": test_user.get("password")
    })
    res_body = res.json()

    assert res.status_code == 200
    assert res_body["token"] is not None


def test_user_login_invalid(test_user: Any) -> None:
    res = client.post("/api/v1/users/login", data={
        "username": test_user.get("email"),
        "password": "Test1235"
    })
    res_body = res.json()

    assert res.status_code == 400
    assert res_body["detail"] == exceptions.INVALID_PASSWORD


# def test_user_gets_token_and_refresh_token(test_user: Any) -> None:
#     login_response = client.post(
#         "/api/v1/users/login",
#         data={"username": test_user["email"], "password": test_user["password"]},
#     )
#     refresh_token = login_response.json()["refresh_token"]
#     response = client.post(
#         "/api/v1/users/refresh",
#         json={"refresh_token": f"{refresh_token}"},
#     )

#     assert response.status_code == 200

#     refresh_token_response = response.json()

#     assert "token" in refresh_token_response
#     assert "refresh_token" in refresh_token_response


# def test_create_reset_token_valid_email(test_user, mocker) -> None:
#     email = test_user.get("email")
#     expected_token = 'valid_token'
#     mocker.patch('jose.jwt.encode', return_value=expected_token)
#     assert create_reset_token(email) == expected_token


# def test_verify_reset_token_invalid_email_format() -> None:
#     invalid_email = 'invalid_email'
#     token = create_reset_token(invalid_email)
#     with pytest.raises(HTTPException) as exc:
#         verify_reset_token(token)
#     assert exc.value.status_code == 400
#     assert exc.value.detail == 'Invalid token'


# def test_verify_reset_token_expired_token() -> None:
#     email = 'test@example.com'
#     delta = timedelta(minutes=-15)
#     now = datetime.now()
#     payload = {
#         'sub': email,
#         'iat': now,
#         'exp': now + delta
#     }
#     expired_token = jwt.encode(payload, settings.SECRET, algorithm=settings.ALGORITHM)
#     with pytest.raises(HTTPException) as exc:
#         verify_reset_token(expired_token)
#     assert exc.value.status_code == 400


# def test_reset_password_invalid_token() -> None:
#     with pytest.raises(HTTPException) as e:
#         reset_password(ResetPasswordRequest(token='invalid_token', new_password='new_password'))
#     assert e.value.status_code == 400
#     assert e.value.detail == 'Invalid token'
