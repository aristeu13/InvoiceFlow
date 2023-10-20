from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    SB_PRIVATE_KEY: str
    SB_ENVIRONMENT: str = "sandbox"
    SB_PROJECT_ID: str
    BROKER_URL: str = "memory://"


settings = Settings()
