from sqlalchemy.ext.asyncio import AsyncSession

from app.models import BusinessTrip
from base.repository import BaseRepository
from app.schemas.business_trips import CreateBusinessTrip
from app.repositories.utils import is_dates_intersects
from base.exceptions import DatesIntersection

class BusinessTripsRepository(BaseRepository):

    def __init__(self):
        self.model = BusinessTrip

    async def save(self, session: AsyncSession, schema: CreateBusinessTrip) -> BusinessTrip:

        if await is_dates_intersects(session,
                                     self.model,
                                     trip_to_check=schema):
                 raise DatesIntersection
        
        await super().save(session, schema)


business_trips_repository = BusinessTripsRepository()