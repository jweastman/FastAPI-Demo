# main.py
"""
FastAPI application entry point.

What lives in main.py?
- App creation: `app = FastAPI(...)` is the single ASGI application object.
- Global setup: configure things once (logging, settings, middleware, CORS, etc.).
- Wiring: include routers so endpoints are registered on the app.

Why include routers?
- Keeps main.py small and readable.
- Lets you split the API into modules (users, orders, payments, etc.).
- Routers can share config like prefixes/tags, and can be tested independently.
"""

from fastapi import FastAPI
from src.core.config import settings
from src.core.logging import setup_logging
from src.routers.my_router import router as users_router

setup_logging()

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health():
    return {"status": "ok", "env": settings.environment}

# Add routers
app.include_router(users_router)
