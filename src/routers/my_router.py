# src/routers/my_router.py
"""
Routers in FastAPI (APIRouter) are a way to group related endpoints together.

Why use routers?
- Keep code organised: all “user” endpoints live together instead of cluttering main.py.
- Reusable modules: you can plug routers into the app with `app.include_router(...)`.
- Shared configuration: apply common `prefix="/users"`, `tags=["users"]`,
  and dependencies (auth, rate limits, etc.) once for the whole group.
- Easier scaling: as your API grows, you add more routers (orders, payments, etc.)
  without turning your app into one huge file.

Example:
- This router owns all endpoints under /users, and main.py will include it.
"""

from fastapi import APIRouter, status
import logging
from src.schemas.my_schemas import CreateUserRequest, CreateUserResponse
from src.services.my_service import UserService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/users", tags=["users"])

_service = UserService()


@router.post("", response_model=CreateUserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(payload: CreateUserRequest) -> CreateUserResponse:
    logger.info("POST /users email=%s", payload.email)
    result = await _service.create_user(payload)
    logger.info("Created user id=%s", result.id)
    return result