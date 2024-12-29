import secrets
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from config import settings

security = HTTPBasic()

def auth_factory(access_level: int):
    
    access_levels = {
        b"root": 0,
        b"admin": 10,
        b"partner": 100
    }

    def auth(
            credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    ):
        
        current_username_bytes = credentials.username.encode("utf8")
            
        try:
            assert access_levels[current_username_bytes]<=access_level
        except KeyError:
                raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
            

        current_password_bytes = credentials.password.encode("utf8")
        match current_username_bytes:    
            case b"root":
                correct_password = settings.ROOT_PASSWORD
            case b"admin":
                correct_password = settings.ADMIN_PASSWORD
            case b"partner":
                correct_password = settings.PARTNER_PASSWORD
        
        is_correct_password = secrets.compare_digest(
        current_password_bytes, bytes(correct_password, "utf8")
        )
        if not is_correct_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username
    return auth

RootDependency = Depends(auth_factory(0))
AdminDependency = Depends(auth_factory(10))
PartnerDependency = Depends(auth_factory(100))