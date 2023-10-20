import base64
from functools import lru_cache
from pydantic_core import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    sb_private_key: str
    sb_environment: str = "sandbox"
    sb_project_id: str

    broker_url: str = "memory://"
    broker_ssl: bool = False
    invoice_start_datetime: str = "2023-10-20T18:00:00-03:00"


@lru_cache  # https://fastapi.tiangolo.com/advanced/settings/#settings-in-a-dependency
def get_settings():
    try:
        return Settings()  # type: ignore
    except ValidationError as ve:
        details = [f'{error["loc"]}: {error["msg"]}' for error in ve.errors()]
        msg = "Failed to load settings:\n" + "\n".join(details)
        raise RuntimeError(msg) from ve
