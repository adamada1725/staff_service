from datetime import date
from typing import Optional
from pydantic import Field

from app.schemas.countries import Country
from base.schema import BaseSchema

class CreatePersonalInfo(BaseSchema):

    first_name: str = Field(min_length=2, max_length=32)

    last_name: Optional[str] = Field(default=None, min_length=2, max_length=64)

    middle_name: Optional[str] = Field(default=None, min_length=2, max_length=64)

    birthdate: Optional[date] = None

    country_id: Optional[int] = None

    sex: Optional[bool] = None

class PersonalInfo(BaseSchema):

    first_name: str = Field(min_length=2, max_length=32)

    last_name: Optional[str] = Field(default=None, min_length=2, max_length=64)

    middle_name: Optional[str] = Field(default=None, min_length=2, max_length=64)

    birthdate: Optional[date] = None

    country: Optional[Country] = None

    sex: Optional[bool] = None

class UpdatePersonalInfo(CreatePersonalInfo):

    pass