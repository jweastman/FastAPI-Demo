

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # These values are defaults
    # That is, if they aren't present in the .env file or as an environment variable
    # the app will go with the defaults below

    app_name: str = "FastAPI Demo"
    environment: str = "dev"   # dev / prod
    log_level: str = "INFO"

    # You can also make environment variables required
    api_key: str  # app fails fast if missing

    # The pattern is:
    # Put non-secret defaults in config.py
    # Put environment-specific stuff / secrets in .env (or real env vars in prod)

@lru_cache
def get_settings() -> Settings:
    return Settings()
