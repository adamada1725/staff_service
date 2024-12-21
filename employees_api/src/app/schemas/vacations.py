from datetime import date
from typing import Optional

from app.schemas.vacation_types import VacationType
from app.schemas.employee_trip import EmployeeTrip

class CreateVacation(EmployeeTrip):

    vacation_type_id: int

class Vacation(EmployeeTrip):

    deleted_at: Optional[date]

    vacation_type: VacationType

class UpdateVacation(CreateVacation):

    pass