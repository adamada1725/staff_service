from abc import ABC
from datetime import date

from pydantic import Field

from base.schema import BaseSchema

class EmployeeTrip(ABC, BaseSchema):

    start_date: date

    end_date: date

    employee_id: int

    reason: str = Field(min_length=2, max_length=128)