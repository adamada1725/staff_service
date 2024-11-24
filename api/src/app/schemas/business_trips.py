from datetime import date
from pydantic import Field
from base.schema import BaseSchema

class CreateBusinessTrip(BaseSchema):

    employee_id: int

    start_date: date

    end_date: date

    city: str = Field(min_length=2, max_length=32)

    reason: str = Field(max_length=128)

class BusinessTrip(BaseSchema):

    start_date: date

    end_date: date

    city: str = Field(min_length=2, max_length=32)

    reason: str = Field(max_length=128)

    id: int

    deleted_at: date

class UpdateBusinessTrip(CreateBusinessTrip):

    pass