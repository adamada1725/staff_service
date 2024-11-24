from datetime import date

from pydantic import Field
from app.schemas.vacation_types import VacationType
from base.schema import BaseSchema

class CreateVacation(BaseSchema):

    employee_id: int

    start_date: date

    end_date: date

    reason: str = Field(min_length=2, max_length=128)

    vacation_type_id: int

class Vacation(BaseSchema):

    id: int

    start_date: date

    end_date: date

    reason: str = Field(min_length=2, max_length=128)

    deleted_at: date | None

    vacation_type: VacationType

class UpdateVacation(CreateVacation):

    pass