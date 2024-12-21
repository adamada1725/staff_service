from typing import Optional

from pydantic import EmailStr, Field

from base.schema import BaseSchema

class CreateConctactInfo(BaseSchema):

    email: Optional[EmailStr] = None

    phone: Optional[str] = Field(default=None, min_length=2, max_length=16)

    tg_id: Optional[str] = Field(default=None, max_length=64)

class ContactInfo(CreateConctactInfo):

    pass

class UpdateContactInfo(CreateConctactInfo):

    pass