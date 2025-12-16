# src/schemas/my_schemas.py
"""
Example service request and response: creating a user.

Benefits of using request/response schemas:
- Validation: FastAPI rejects bad input automatically (422).
- Better docs: Swagger shows fields + examples.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class CreateUserRequest(BaseModel):
    """What the client sends to create a user."""
    email: EmailStr = Field(example="alice@example.com")
    name: str = Field(min_length=1, example="Alice")


class CreateUserResponse(BaseModel):
    """What your API returns after creating the user."""
    id: UUID
    email: EmailStr
    name: str
    created_at: datetime = Field(example="2025-12-16T12:34:56Z")