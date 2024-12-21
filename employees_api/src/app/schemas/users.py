import datetime
from typing import Optional

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

    deleted_at: Optional[datetime.datetime]

class UpdateUser(CreateUser):

    id: int