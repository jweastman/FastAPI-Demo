from fastapi import APIRouter, status

from src.schemas.my_schemas import CreateUserRequest, CreateUserResponse
from services.my_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

_service = UserService()


@router.post("", response_model=CreateUserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(payload: CreateUserRequest) -> CreateUserResponse:
    return await _service.create_user(payload)