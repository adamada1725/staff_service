import datetime

from pydantic import Field

from base.schema import BaseSchema


class CreateUser(BaseSchema):

    login: str = Field(min_length=4, max_length=32)

    password: str = Field(min_length=8, max_length=32)

    role_id: int

class UserSchema(BaseSchema):

    login: str = Field(min_length=4, max_length=32)

    id: int

    created_at: datetime.datetime

    deleted_at: datetime.datetime | None

class UpdateUser(CreateUser):

    id: int