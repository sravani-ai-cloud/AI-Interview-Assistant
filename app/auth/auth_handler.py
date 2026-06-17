from app.database.db import SessionLocal
from app.database.user_crud import (
    get_user_by_username,
    create_user
)
from jose import jwt
from datetime import datetime, timedelta
import os
from app.auth.password_handler import (
    hash_password,
    verify_password
)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"


def register_user(username, password):

    db = SessionLocal()

    existing_user = get_user_by_username(
        db,
        username
    )

    if existing_user:
        return {"message": "User already exists"}

    hashed_password = hash_password(password)

    create_user(
        db,
        username,
        hashed_password
    )

    return {
        "message": "User registered successfully"
    }

def login_user(username, password):

    db = SessionLocal()

    user = get_user_by_username(
        db,
        username
    )

    if not user:
        return {"message": "Invalid username"}

    if not verify_password(
        password,
        user.password
    ):
        return {"message": "Invalid password"}

    token = jwt.encode(
        {
            "sub": username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }