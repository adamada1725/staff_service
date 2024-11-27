from functools import wraps

from fastapi import Response, status
from sqlalchemy.exc import NoResultFound

from config import settings

def handle_exceptions(func):
    
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except NoResultFound:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            if settings.ECHO:
                return Response(str(e), status_code=500)
            else:
                return Response(status_code=500)
    
    return wrapper