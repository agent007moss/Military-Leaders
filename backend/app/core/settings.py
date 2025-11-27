from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "Military Leaders Tool Backend"
    API_PREFIX: str = "/api"

    # Security
    SECRET_KEY: str = "CHANGE_ME"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Database
    DATABASE_URL: str = "sqlite:///./mlt.db"

    class Config:
        env_file = ".env"
        extra = "allow"


@lru_cache()
def get_settings():
    return Settings()

