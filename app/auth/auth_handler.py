from jose import jwt
from datetime import datetime, timedelta
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

# Temporary user storage
users_db = {}

def register_user(username, password):

    if username in users_db:
        return {"message": "User already exists"}

    users_db[username] = password

    return {"message": "User registered successfully"}

def login_user(username, password):

    if username not in users_db:
        return {"message": "Invalid username"}

    if users_db[username] != password:
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