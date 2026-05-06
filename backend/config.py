from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings

from app_types import AppRunningMode

from dotenv import load_dotenv

load_dotenv()

"""
Execute in console to manually run postgres docker image
    docker run --name clockly_postgres_container
    -e POSTGRES_USER=database
    -e POSTGRES_PASSWORD=password
    -e POSTGRES_DB=prod
    -p 5432:5432
    -d postgres
"""

# TODO: refactor for best practices


class Settings(BaseSettings):
    app_mode: AppRunningMode = "prod"

    # auth
    jwt_secret: str = Field(
        validation_alias="JWT_SECRET_KEY"
    )  # will be imported from .env
    access_jwt_expiry_seconds: int = 3600
    refresh_jwt_expiry_seconds: int = 172800

    # logging
    logging_filename: str = "logs.log"
    logger_name: str = "clockly_logger"
    LOGGING_FORMAT: str = "%(levelname)s (%(asctime)s): %(message)s"

    # postgres
    postgres_dsn_prod: PostgresDsn = Field(
        validation_alias="POSTGRES_DSN_PROD"
    )
    postgres_dsn_test: PostgresDsn = Field(
        validation_alias="POSTGRES_DSN_TEST"
    )

    # app
    pagination: int = 30
    export_chunks_size: int = 2

    def get_postgres_dsn(self) -> PostgresDsn:
        """Returns postgresql DSN regarding to the app_mode variable"""

        match self.app_mode:
            case "prod":
                return self.postgres_dsn_prod
            case "test":
                return self.postgres_dsn_test


settings = Settings()
