from fastapi import FastAPI
from src.core.config import get_settings
from src.routers.my_router import router as users_router

settings = get_settings()

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health():
    return {"status": "ok", "env": settings.environment}

# Add routers
app.include_router(users_router)
