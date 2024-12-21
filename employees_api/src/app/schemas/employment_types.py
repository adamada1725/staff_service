from pydantic import Field
from base.schema import BaseSchema

class CreateEmploymentType(BaseSchema):

    title: str = Field(min_length=2, max_length=64)

class EmploymentTypeSchema(CreateEmploymentType):

    id: int

class UpdateEmploymentType(CreateEmploymentType):

    pass