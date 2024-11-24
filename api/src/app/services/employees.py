from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Employee as EmployeeModel
from app.repositories.employees import employee_repository
from app.repositories.personal_info import personal_info_repository
from app.repositories.contact_info import contact_info_repository
from app.schemas.employees import CreateEmployee, Employee, UpdateEmployee

class EmployeeService:

    _repo = employee_repository
    
    @classmethod
    async def save(cls, session: AsyncSession, schema: CreateEmployee):

        e_id  = (await cls._repo.save(session, schema.base)).user_id

        await personal_info_repository.save(session, schema.personal_info, e_id)
        await contact_info_repository.save(session, schema.contact_info, e_id)
        

    @classmethod
    async def get_all(cls, session: AsyncSession, full: bool):

        response = await cls._repo.find_all(session, full=full)

        return response

    @classmethod
    async def get_one(cls, session: AsyncSession, id: int):

        response = await cls._repo.find_by_id(session, id)

        return response
    
    @classmethod
    async def delete_one(cls, session: AsyncSession, id: int):

        await cls._repo.delete_by_id(session, id)
        
    @classmethod
    async def update_one(cls, session: AsyncSession, id: int, employee_schema: UpdateEmployee):
        
        await cls._repo.find_by_id(session, id)
        return await cls._repo.update_by_id(session, id, employee_schema)
