from typing import Annotated, List, Optional, Sequence
from fastapi import Depends, Path, Query, Response, status
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.schemas.departments import CreateDepartment, UpdateDepartment
from app.repositories.departments import department_repository
from base.database import session_dependency

departments_router = APIRouter(prefix="/departments", tags=["departments"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]

@departments_router.get("")
async def get_departments(session: SessionDependency,
                          order_by: str = "id",
                          limit: int = 100):
    
    return await department_repository.find_all(session, order_by, limit)

@departments_router.get("/{department_id}")
async def get_department_by_id(department_id: Annotated[int, Path(ge=1)],
                               session: SessionDependency):
    try:
        return await department_repository.find_by_id(session, department_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@departments_router.post("")
async def create_department(session: SessionDependency,
                            department_schema: CreateDepartment):
    
    return await department_repository.save(session, department_schema)

@departments_router.delete("/{department_id}")
async def delete_department_by_id(department_id: Annotated[int, Path(ge=1)],
                                  session: SessionDependency):
    
    try:
        await department_repository.delete_by_id(session, department_id)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@departments_router.patch("/{department_id}")
async def update_department_by_id(department_id: Annotated[int, Path(ge=1)],
                            schema: UpdateDepartment,
                            session: SessionDependency):
    
    try:
        await department_repository.update_by_id(session, department_id, schema)
    except NoResultFound:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
        