from typing import Annotated
from fastapi import Depends, Path
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.vacations import CreateVacation, UpdateVacation
from app.repositories.vacations import vacations_repository
from base.database import session_dependency
from base.utils.router_exception_handler import handle_exceptions

vacations_router = APIRouter(prefix="/vacations", tags=["vacations"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]

@vacations_router.get("")
@handle_exceptions
async def get_vacations(session: SessionDependency,
                          order_by: str = "id",
                          limit: int = 100):
    
    return await vacations_repository.find_all(session, order_by, limit)

@vacations_router.get("/{vacation_id}")
@handle_exceptions
async def get_vacation_by_id(vacation_id: Annotated[int, Path(ge=1)],
                             session: SessionDependency):
    
    return await vacations_repository.find_by_id(session, vacation_id)

@vacations_router.post("")
@handle_exceptions
async def create_vacation(session: SessionDependency,
                          vacation_schema: CreateVacation):
    
    return await vacations_repository.save(session, vacation_schema)

@vacations_router.delete("/{vacation_id}")
@handle_exceptions
async def delete_vacation_by_id(vacation_id: Annotated[int, Path(ge=1)],
                                  session: SessionDependency):
    
    await vacations_repository.delete_by_id(session, vacation_id)

@vacations_router.patch("/{vacation_id}")
@handle_exceptions
async def update_vacation_by_id(vacation_id: Annotated[int, Path(ge=1)],
                            schema: UpdateVacation,
                            session: SessionDependency):
    
    await vacations_repository.update_by_id(session, vacation_id, schema)
        