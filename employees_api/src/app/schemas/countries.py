from pydantic import Field
from base.schema import BaseSchema

class CreateCountry(BaseSchema):

    title: str = Field(min_length=2, max_length=64)

class Country(CreateCountry):

    id: int

class UpdateCountry(CreateCountry):

    pass