from typing import Annotated, TypeVar

from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from base.repositories import BaseRepository
from base.database import Database
from base.utils.router_exceptions_handler import handle_exceptions

Repo = TypeVar("Repo", bound=BaseRepository)

R = TypeVar("R", bound=APIRouter)

SessionDependency = Annotated[AsyncSession, Depends(Database.session_dependency)]

def BaseRouterFactory(router: R, repository: Repo):

    @router.get("")
    @handle_exceptions
    async def get(session: SessionDependency):

        return await repository.find_all(session)
    
    @router.get("/{id}")
    @handle_exceptions
    async def get_by_id(id: Annotated[int, Path()],
                        session: SessionDependency):
        
        return await repository.find_by_id(session, id=id)
    
    @router.post("")
    @handle_exceptions
    async def post(schema: repository.schemas.CreateSchema,
                   session: SessionDependency):
        
        return await repository.save(session, schema)
    
    @router.delete("/{id}")
    @handle_exceptions
    async def delete(id: Annotated[int, Path()],
                     session: SessionDependency):
        
        return await repository.delete_by_id(session, id)
    
    @router.patch("/{id}")
    @handle_exceptions
    async def patch(id: Annotated[int, Path()],
                    session: SessionDependency,
                    schema: repository.schemas.UpdateSchema):
        
        return await repository.update_by_id(session, id, schema)
    
    return [get, get_by_id, post, delete, patch]
