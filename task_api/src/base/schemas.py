from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, create_model

class BaseSchema(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    @classmethod
    def with_fields(cls, **field_definitions):
        return create_model('ModelWithFields', __base__=cls, **field_definitions)


class BaseInstance:

    class Base(BaseSchema):
        
        name: str

        description: str = None

        created_by: int

    class CreateSchema(Base):

        pass

    class UpdateSchema(Base):
        
        pass

    class GetSchema(Base):

        id: int

        created_at: datetime

        deleted_at: Optional[datetime] = None