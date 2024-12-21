from app.models import BusinessTrip
from base.repository import BaseTripRepository

class BusinessTripsRepository(BaseTripRepository):
    pass

business_trips_repository = BusinessTripsRepository(BusinessTrip)