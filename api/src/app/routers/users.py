from typing import Annotated, List, Optional, Sequence
from fastapi import Depends, Path, Query, Response, status
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.repositories.users import user_repository
from base.database import session_dependency
from app.schemas.users import CreateUser, UpdateUser

users_router = APIRouter(prefix="/users", tags=["users"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]

@users_router.get("")
async def get_users(session: SessionDependency,
                    order_by: str = "id",
                    limit: int = 100):
    
    return await user_repository.find_all(session, order_by, limit)

@users_router.get("/{user_id}")
async def get_user_by_id(user_id: Annotated[int, Path(ge=1)],
                         session: SessionDependency):
    try:
        return await user_repository.find_by_id(session, user_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@users_router.post("")
async def create_user(session: SessionDependency,
                      user_schema: CreateUser):
    
    return await user_repository.save(session, user_schema)

@users_router.delete("/{user_id}")
async def delete_user_by_id(user_id: Annotated[int, Path(ge=1)],
                            session: SessionDependency):
    
    try:
        await user_repository.delete_by_id(session, user_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@users_router.patch("/{user_id}")
async def update_user_by_id(user_id: Annotated[int, Path(ge=1)],
                            schema: UpdateUser,
                            session: SessionDependency):
    
    try:
        await user_repository.update_by_id(session, user_id, schema)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
        