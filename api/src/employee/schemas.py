from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict

class EmployeeBase(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    country_id: int
    
    department_id: Optional[int]

    first_name: str

    last_name: Optional[str]

    middle_name: Optional[str]
    
    sex_id: int

    login: str

    password: str

    email: Optional[str]

    phone: Optional[str]

    employment_type_id: int

class Employee(EmployeeBase):

    id: int
    
    created_at: date

    deleted_at: Optional[date]

class CreateEmployee(EmployeeBase):
    pass

class UpdateEmployee(CreateEmployee):
    pass

class Country(BaseModel):
    
    id: int
    
    title: str

class CreateCountry(BaseModel):
    
    title: str

class UpdateCountry(CreateCountry):
    pass

class Department(BaseModel):
    
    id: int
    
    title: str

class CreateDepartment(BaseModel):
    
    title: str