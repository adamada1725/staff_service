from pydantic import Field
from base.schema import BaseSchema

class CreateVacationType(BaseSchema):

    title: str = Field(min_length=2, max_length=64)

class VacationType(CreateVacationType):

    id: int

class UpdateVacationType(CreateVacationType):
    
    pass