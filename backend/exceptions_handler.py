from fastapi import HTTPException
from functools import wraps
from logger import logger

# import bcrypt
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from jwt.exceptions import PyJWKError

# Bcrypt - UnicodeEncodeError, UnicodeDecodeError 

def endpoint_exception_handler(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as e:
            raise e from e

        except SQLAlchemyError as e:
            logger.error("SQLAlchemy Error", exc_info=e)
            raise HTTPException(
                status_code=500, 
                detail="Internal Server Error"
            )

        except (UnicodeEncodeError, UnicodeDecodeError) as e:
            logger.error("Bcrypt Error", exc_info=e)
            raise HTTPException(
                status_code=500, 
                detail="Internal Server Error"
            )

        except PyJWKError as e:
            logger.error("PyJWT Error", exc_info=e)
            raise HTTPException(
                status_code=401, 
                detail="Unauthorized"
            )

        except ValueError as e:
            logger.error("ValueError", exc_info=e)
            raise HTTPException(
                status_code=500, 
                detail="Internal Server Error"
            )

        except Exception as e:
            logger.error("Exception", exc_info=e)
            raise HTTPException(
                status_code=500, 
                detail="Internal Server Error"
            )
        
    return wrapper
