# src/services/my_service.py
"""
Services in a FastAPI project are where “business logic” lives.

Why use a service layer?
- Keeps routers thin: routers handle HTTP concerns (request/response/status codes),
  while services handle the actual work (create user, call DB, etc.).
- Easier to test: you can unit test the service without running FastAPI.
- Reusable logic: the same service method can be used by multiple endpoints.
- Clear separation of concerns: routing != business rules.

In a real app this service would talk to a database, external APIs,
or other components. Here, it just returns a pretend created user.
"""

from datetime import datetime, timezone
from uuid import uuid4
import logging
from src.schemas.my_schemas import CreateUserRequest, CreateUserResponse
logger = logging.getLogger(__name__)

class UserService:
    async def create_user(self, req: CreateUserRequest) -> CreateUserResponse:
        # Actual business logic takes place in services
        # Sadly, that is out of scope of this repo
        
        logger.debug("Service creating user name=%s", req.name)
        return CreateUserResponse(
            id=uuid4(),
            email=req.email,
            name=req.name,
            created_at=datetime.now(timezone.utc),
        )