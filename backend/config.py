from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    app_mode: Literal["prod", "test"]

    # auth
    jwt_secret: str = Field(validation_alias="JWT_SECRET_KEY")

    # logging
    logging_filename: str = "logs.log"
    logger_name: str = "clockly_logger"
    LOGGING_FORMAT: str = "%(levelname)s (%(asctime)s): %(message)s"

    # postgres
    postgres_dsn_prod: PostgresDsn = "postgresql+asyncpg://database:password@localhost:5432/prod"
    postgres_dsn_test: PostgresDsn = "postgresql+asyncpg://database:password@localhost:5432/test"

    # app
    pagination: int = 30

    @classmethod
    def get_postgres_dsn(cls) -> PostgresDsn:
        """Returns postgresql DSN regarding to the app_mode variable"""

        match cls.app_mode: 
            case "prod":
                return cls.postgres_dsn_prod
            case "test":
                return cls.postgres_dsn_test


settings = Settings()
