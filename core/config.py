"""
Configuration settings for the application
"""
import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    PROJECT_NAME: str = "School Management App"
    PROJECT_VERSION: str = "0.1.0"
    # Database Settings
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")
    POSTGRES_PORT: int = os.environ.get("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    POSTGRES_TEST_DB: str = os.environ.get("POSTGRES_TEST_DB")
    DATABASE_URL: str | None = os.environ.get(
        "DATABASE_URL",
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
    # App specific
    SECRET: str = os.environ.get("SECRET", "b7XaffRQ4eU9QV3BeopyxCJw89LhJo")
    REFRESH_SECRET: str = os.environ.get("REFRESH_SECRET", "jYZVNrAZr2aBLHvTqb3prHer5g6RJk")
    PRODUCTION_ENV: bool = False
    REFRESH_TOKEN_EXPIRE_MINUTES: int = os.environ.get(
        "REFRESH_TOKEN_EXPIRE_MINUTES", 60 * 30 * 24
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.environ.get(
        "ACCESS_TOKEN_EXPIRE_MINUTES", 60 * 30 * 24
    )
    ALGORITHM: str = os.environ.get("ALGORITHM", "HS256")
    BASE_URL: str = os.environ.get("BASE_URL")
    # Email settings
    EMAIL_SERVER: str = os.environ.get("EMAIL_SERVER")
    EMAIL_PORT: int = os.environ.get("EMAIL_PORT")
    EMAIL_SENDER: str = os.environ.get("EMAIL_SENDER")
    EMAIL_PASSWORD: str = os.environ.get("EMAIL_PASSWORD")
    URL_PATH: str


settings = Settings()
