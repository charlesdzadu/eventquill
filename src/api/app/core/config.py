from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    APP_NAME: str = "Event Quill"


class EnvSettings(Settings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

    MASTER_ACCESS_KEY: str
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
    MONGO_URI: str
    MONGO_DB_NAME: str


envSettings = EnvSettings()
