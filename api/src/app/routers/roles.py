from typing import Annotated
from fastapi import Depends, Path, Response, status
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from base.database import session_dependency
from app.schemas.roles import CreateRole
from app.services.roles import RoleService
from base.utils.router_exception_handler import handle_exceptions

router = APIRouter(prefix="/roles", tags=["roles"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]


@router.get("")
@handle_exceptions
async def get_roles(session: SessionDependency):

    return await RoleService.get_all(session)

@router.get("/{role_id}")
@handle_exceptions
async def get_one_role(role_id: Annotated[int, Path(ge=1)],
                       session: SessionDependency):

    return await RoleService.get_one(session, role_id)

@router.post("")
@handle_exceptions
async def create_role(role_schema: CreateRole,
                      session: SessionDependency):
    
    return await RoleService.save(session, role_schema)

@router.delete("/{role_id}")
@handle_exceptions
async def delete_role(role_id: Annotated[int, Path()],
                      session: SessionDependency):
    
    await RoleService.delete_one(session, role_id)

@router.patch("/{role_id}")
@handle_exceptions
async def update_role(role_id: Annotated[int, Path()],
                      schema: CreateRole,
                      session: SessionDependency):
    
    await RoleService.update_one(session, role_id, schema)