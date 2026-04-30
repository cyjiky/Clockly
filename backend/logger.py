import logging
from config import settings

logger = logging.getLogger(settings.logger_name)

logging.basicConfig(
    filename=settings.logging_filename,
    format=settings.LOGGING_FORMAT,
    level=logging.INFO

)

if __name__ == "__main__":
    logger.log(level=logging.FATAL, msg="Well well well...",)