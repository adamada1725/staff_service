from datetime import date

from pydantic import Field

from app.schemas.employee_trip import EmployeeTrip

class CreateBusinessTrip(EmployeeTrip):

    city: str = Field(min_length=2, max_length=32)

class BusinessTrip(EmployeeTrip):

    city: str = Field(min_length=2, max_length=32)

    id: int

    deleted_at: date

class UpdateBusinessTrip(CreateBusinessTrip):

    pass