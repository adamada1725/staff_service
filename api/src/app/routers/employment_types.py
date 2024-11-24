from typing import Annotated, List, Optional, Sequence
from fastapi import Depends, Path, Query, Response, status
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.schemas.employment_types import CreateEmploymentType, UpdateEmploymentType
from app.repositories.employment_types import employment_types_repository
from base.database import session_dependency

employment_types_router = APIRouter(prefix="/employment_types", tags=["employment_types"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]

@employment_types_router.get("")
async def get_employment_types(session: SessionDependency,
                               order_by: str = "id",
                               limit: int = 100):
    
    return await employment_types_repository.find_all(session, order_by, limit)

@employment_types_router.get("/{employment_type_id}")
async def get_employment_types_by_id(employment_type_id: Annotated[int, Path(ge=1)],
                                     session: SessionDependency):
    try:
        return await employment_types_repository.find_by_id(session, employment_type_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@employment_types_router.post("")
async def create_employment_type(session: SessionDependency,
                                 department_schema: CreateEmploymentType):
    
    return await employment_types_repository.save(session, department_schema)

@employment_types_router.delete("/{employment_type_id}")
async def delete_employment_type_by_id(employment_type_id: Annotated[int, Path(ge=1)],
                                       session: SessionDependency):
    
    try:
        await employment_types_repository.delete_by_id(session, employment_type_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@employment_types_router.patch("/{employment_type_id}")
async def update_employment_type_by_id(employment_type_id: Annotated[int, Path(ge=1)],
                                       schema: UpdateEmploymentType,
                                       session: SessionDependency):
    
    try:
        await employment_types_repository.update_by_id(session, employment_type_id, schema)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
        