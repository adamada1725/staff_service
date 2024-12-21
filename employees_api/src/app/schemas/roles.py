from pydantic import Field

from base.schema import BaseSchema


class CreateRole(BaseSchema):

    title: str = Field(min_length=3, max_length=32)

    token: str = Field(min_length=8, max_length=64)


class Role(CreateRole):
    
    id: int = Field(ge=1)


class UpdateRole(Role):

    pass