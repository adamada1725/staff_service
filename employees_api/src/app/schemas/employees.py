from typing import List, Optional
from app.schemas.employment_types import EmploymentTypeSchema
from app.schemas.position_types import PositionType
from app.schemas.contact_info import ContactInfo, CreateConctactInfo
from app.schemas.personal_info import CreatePersonalInfo, PersonalInfo
from app.schemas.users import UserSchema
from app.schemas.departments import DeaprtmentSchema
from base.schema import BaseSchema

class BaseCreateEmployee(BaseSchema):

    user_id: int

    department_id: Optional[int] = None

    employment_type_id: Optional[int] = None

class CreateEmployee(BaseSchema):

    base: BaseCreateEmployee

    personal_info: Optional[CreatePersonalInfo] = None

    contact_info: Optional[CreateConctactInfo] = None

    position_types_id: Optional[List[int]] = None

    

class Employee(BaseSchema):

    user: UserSchema

    department: Optional[DeaprtmentSchema] = None

    employment_type: Optional[EmploymentTypeSchema] = None

    personal_info: Optional[PersonalInfo] = None

    contact_info: Optional[ContactInfo] = None

    positions: Optional[List[PositionType]] = None

class UpdateEmployee(CreateEmployee):

    pass