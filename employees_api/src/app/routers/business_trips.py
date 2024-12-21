from typing import Annotated
from fastapi import Depends, Path
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.business_trips import CreateBusinessTrip, UpdateBusinessTrip
from app.repositories.business_trips import business_trips_repository
from base.database import session_dependency
from base.utils.router_exception_handler import handle_exceptions

business_trips_router = APIRouter(prefix="/business_trips", tags=["business_trips"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]

@business_trips_router.get("")
@handle_exceptions
async def get_business_trips(session: SessionDependency,
                          order_by: str = "id",
                          limit: int = 100):
    
    return await business_trips_repository.find_all(session, order_by, limit)

@business_trips_router.get("/{business_trip_id}")
@handle_exceptions
async def get_business_trip_by_id(business_trip_id: Annotated[int, Path(ge=1)],
                             session: SessionDependency):
    
    return await business_trips_repository.find_by_id(session, business_trip_id)

@business_trips_router.post("")
@handle_exceptions
async def create_business_trip(session: SessionDependency,
                          business_trip_schema: CreateBusinessTrip):
    
    return await business_trips_repository.save(session, business_trip_schema)

@business_trips_router.delete("/{business_trip_id}")
@handle_exceptions
async def delete_business_trip_by_id(business_trip_id: Annotated[int, Path(ge=1)],
                                  session: SessionDependency):
    
    await business_trips_repository.delete_by_id(session, business_trip_id)

@business_trips_router.patch("/{business_trip_id}")
@handle_exceptions
async def update_business_trip_by_id(business_trip_id: Annotated[int, Path(ge=1)],
                            schema: UpdateBusinessTrip,
                            session: SessionDependency):
    
    await business_trips_repository.update_by_id(session, business_trip_id, schema)
        