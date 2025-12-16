from datetime import datetime, timezone
from uuid import uuid4

from src.schemas.my_schemas import CreateUserRequest, CreateUserResponse


class UserService:
    async def create_user(self, req: CreateUserRequest) -> CreateUserResponse:
        # pretend work happens here (db, api call, etc.)
        return CreateUserResponse(
            id=uuid4(),
            email=req.email,
            name=req.name,
            created_at=datetime.now(timezone.utc),
        )