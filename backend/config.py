from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # TODO ENV


    # logging
    logging_filename: str = "logs.log"
    logger_name: str = "clockly_logger"
    LOGGING_FORMAT: str = "%(levelname)s (%(asctime)s): %(message)s"

settings = Settings()
