from typing import Annotated
from fastapi import Depends, Path
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from base.database import session_dependency
from app.schemas.position_types import CreatePositionType, UpdatePositionType
from app.repositories.position_types import position_type_repository
from base.utils.router_exception_handler import handle_exceptions

position_type_router = APIRouter(prefix="/position_types", tags=["position_types"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]


@position_type_router.get("")
@handle_exceptions
async def get_position_types(session: SessionDependency):

    return await position_type_repository.find_all(session)

@position_type_router.get("/{position_type_id}")
@handle_exceptions
async def get_one_position_type(position_type_id: Annotated[int, Path(ge=1)],
                                session: SessionDependency):

    return await position_type_repository.find_by_id(session, position_type_id)

@position_type_router.post("")
@handle_exceptions
async def create_position_type(position_type_schema: CreatePositionType,
                         session: SessionDependency):
    
    return await position_type_repository.save(session, position_type_schema)

@position_type_router.delete("/{position_type_id}")
@handle_exceptions
async def delete_position_type(position_type_id: Annotated[int, Path()],
                         session: SessionDependency):
    
    await position_type_repository.delete_by_id(session, position_type_id)

@position_type_router.patch("/{position_type_id}")
@handle_exceptions
async def update_position_type(position_type_id: Annotated[int, Path()],
                               schema: UpdatePositionType,
                               session: SessionDependency):
    
    await position_type_repository.update_by_id(session, position_type_id, schema)