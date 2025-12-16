# src/utils/create_user_utils.py
"""
utils: small helper functions used across the app.

I like to break these up per task

Why have a per-task utils module?
- Keeps helpers close to the “feature/task” they support.
- Avoids one giant utils.py that becomes a dumping ground.
- Makes it easy to find and delete helpers later if the task is removed.

Note:
- This is as an example of how you’d structure helpers.
"""

from datetime import datetime, timezone
from uuid import UUID


def utc_now() -> datetime:
    """Return a timezone-aware UTC timestamp."""
    return datetime.now(timezone.utc)


def is_valid_uuid(value: str) -> bool:
    """Return True if the string is a valid UUID, otherwise False."""
    try:
        UUID(value)
        return True
    except ValueError:
        return False


def clean_string(value: str) -> str:
    """Trim whitespace and collapse repeated internal spaces."""
    return " ".join(value.strip().split())
