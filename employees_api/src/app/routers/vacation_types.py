from typing import Annotated
from fastapi import Depends, Path
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from base.database import session_dependency
from app.schemas.vacation_types import CreateVacationType, UpdateVacationType
from app.repositories.vacation_types import vacation_type_repository
from base.utils.router_exception_handler import handle_exceptions

vacation_type_router = APIRouter(prefix="/vacation_types", tags=["vacation_types"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]


@vacation_type_router.get("")
@handle_exceptions
async def get_vacation_types(session: SessionDependency):

    return await vacation_type_repository.find_all(session)

@vacation_type_router.get("/{vacation_type_id}")
@handle_exceptions
async def get_one_vacation_type(vacation_type_id: Annotated[int, Path(ge=1)],
                                session: SessionDependency):

    return await vacation_type_repository.find_by_id(session, vacation_type_id)

@vacation_type_router.post("")
@handle_exceptions
async def create_vacation_type(vacation_type_schema: CreateVacationType,
                               session: SessionDependency):
    
    return await vacation_type_repository.save(session, vacation_type_schema)

@vacation_type_router.delete("/{vacation_type_id}")
@handle_exceptions
async def delete_vacation_type(vacation_type_id: Annotated[int, Path()],
                               session: SessionDependency):
    
    await vacation_type_repository.delete_by_id(session, vacation_type_id)

@vacation_type_router.patch("/{vacation_type_id}")
@handle_exceptions
async def update_vacation_type(vacation_type_id: Annotated[int, Path()],
                               schema: UpdateVacationType,
                               session: SessionDependency):
    
    await vacation_type_repository.update_by_id(session, vacation_type_id, schema)