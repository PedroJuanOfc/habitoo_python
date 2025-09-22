from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    jwt_secret: str = Field(..., alias="JWT_SECRET")
    jwt_alg: str = Field(default="HS256", alias="JWT_ALG")
    access_token_expires_min: int = Field(default=60, alias="ACCESS_TOKEN_EXPIRES_MIN")
    app_name: str = "Habitoo API"
    app_version: str = "0.1.0"
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()
settings: Settings = get_settings()
