from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings

from app_types import AppRunningMode

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_mode: AppRunningMode = "prod"

    # auth
    jwt_secret: str = Field(validation_alias="JWT_SECRET_KEY") # will be imported from .env
    access_jwt_expiry_seconds: int = 3600
    refresh_jwt_expiry_seconds: int = 172800

    # logging
    logging_filename: str = "logs.log"
    logger_name: str = "clockly_logger"
    LOGGING_FORMAT: str = "%(levelname)s (%(asctime)s): %(message)s"

    # postgres
    postgres_dsn_prod: PostgresDsn = "postgresql+asyncpg://database:password@localhost:5432/prod"
    postgres_dsn_test: PostgresDsn = "postgresql+asyncpg://database:password@localhost:5432/test"

    # app
    pagination: int = 30

    def get_postgres_dsn(self) -> PostgresDsn:
        """Returns postgresql DSN regarding to the app_mode variable"""

        match self.app_mode: 
            case "prod":
                return self.postgres_dsn_prod
            case "test":
                return self.postgres_dsn_test


settings = Settings()
