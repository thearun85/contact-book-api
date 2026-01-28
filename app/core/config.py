"""Application configuration using Pydantic settings.
Loads and validates environment variables.
"""
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Literal

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    # Flask configuration
    flask_env: Literal["development", "testing", "production"] = "development"
    flask_app: str = "app:create_app"
    debug: bool = True

    # Database configuration
    database_url: str = Field(
        default="postgresql:postgres:postgres@localhost:5432/contactbook",
        description="PostgreSQL connection string"
    )

    # Security
    secret_key: str = Field(
        default="default-key-change-this-in-production",
        min_length=32,
        description="Secret key for session encryption"
    )

    # Logging
    log_level:  Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]= "INFO"
    

    # Application metadata
    app_name: str = "Contact Book API"
    app_version: str = "2.0.0"

    # Model configuration
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        case_sensitive = False,
        extra = "ignore" # ignore extra env variables not defined here
    )

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, url:str) -> str:
        """Validate database_url starts with postgresql://"""
        if not url.startswith("postgresql://"):
            raise ValueError("Database URL must start with postgresql://")
        return url

    @field_validator("secret_key")
    @classmethod
    def validate_secret_key(cls, key:str) -> str:
        """Warn if using default secret key"""
        if key == "change-this-in-production":
            import warnings
            warnings.warn(
                "Using default secret key! Change this in production!",
                UserWarning
            )
        return key
    
@lru_cache
def get_settings() -> Settings:
    """
    Create and cache settings instance.

    @lru_cache ensures we only create one settings object
    for the entire application lifecycle (singleton pattern).

    Returns:
        Settings: Validated configuration object
    """
    return Settings()

settings = get_settings()
