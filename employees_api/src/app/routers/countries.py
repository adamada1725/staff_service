from typing import Annotated
from fastapi import Depends, Path
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from base.database import session_dependency
from app.schemas.countries import CreateCountry, UpdateCountry
from app.repositories.countries import country_repository
from base.utils.router_exception_handler import handle_exceptions

router = APIRouter(prefix="/countries", tags=["countries"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]


@router.get("")
@handle_exceptions
async def get_countries(session: SessionDependency):

    return await country_repository.find_all(session, limit=300)

@router.get("/{country_id}")
@handle_exceptions
async def get_one_country(country_id: Annotated[int, Path(ge=1)],
                       session: SessionDependency):

    return await country_repository.find_by_id(session, country_id)

@router.post("")
@handle_exceptions
async def create_country(country_schema: CreateCountry,
                         session: SessionDependency):
    
    return await country_repository.save(session, country_schema)

@router.delete("/{country_id}")
@handle_exceptions
async def delete_country(country_id: Annotated[int, Path()],
                         session: SessionDependency):
    
    await country_repository.delete_by_id(session, country_id)

@router.patch("/{country_id}")
@handle_exceptions
async def update_country(country_id: Annotated[int, Path()],
                         schema: UpdateCountry,
                         session: SessionDependency):
    
    await country_repository.update_by_id(session, country_id, schema)