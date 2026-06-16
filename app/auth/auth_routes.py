from fastapi import APIRouter
from fastapi import Header

from app.auth.token_validator import verify_token

from app.models.auth_request import (
    RegisterRequest,
    LoginRequest
)

from app.auth.auth_handler import (
    register_user,
    login_user
)

router = APIRouter()

@router.post("/register")
def register(request: RegisterRequest):

    return register_user(
        request.username,
        request.password
    )

@router.post("/login")
def login(request: LoginRequest):

    return login_user(
        request.username,
        request.password
    )

@router.get("/profile")
def profile(token: str):

    payload = verify_token(token)

    if not payload:
        return {"message": "Invalid token"}

    return {
        "message": "Access Granted",
        "user": payload["sub"]
    }
    