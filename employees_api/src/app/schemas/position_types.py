from pydantic import Field
from base.schema import BaseSchema

class CreatePositionType(BaseSchema):

    title: str = Field(min_length=2, max_length=64)

class PositionType(CreatePositionType):

    id: int

class UpdatePositionType(CreatePositionType):
    
    pass