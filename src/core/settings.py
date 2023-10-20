from functools import lru_cache
from pydantic_core import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    SB_PRIVATE_KEY: str
    SB_ENVIRONMENT: str = "sandbox"
    SB_PROJECT_ID: str
    BROKER_URL: str = "memory://"


@lru_cache  # https://fastapi.tiangolo.com/advanced/settings/#settings-in-a-dependency
def get_settings():
    try:
        return Settings()  # type: ignore
    except ValidationError as ve:
        details = [f'{error["loc"]}: {error["msg"]}' for error in ve.errors()]
        msg = "Failed to load settings:\n" + "\n".join(details)
        raise RuntimeError(msg) from ve
