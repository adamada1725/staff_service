from typing import Optional, List, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models import Employee
from base.repository import BaseRepository

M = TypeVar("M", bound=Employee)

class EmployeeRepository(BaseRepository):
    
    def __init__(self):
        self.model = Employee

    async def find_all(self, 
                       session: AsyncSession,
                       order_by: str = "user_id", 
                       limit: int = 100,
                       unique: bool = False,
                       full: bool = True,
                       **filters) -> Optional[List[Employee]]:

        stmt = select(self.model)

        if full:
                stmt = stmt.options(joinedload(self.model.contact_info), joinedload(self.model.personal_info))

        stmt = (stmt
                .filter_by(**filters)
                .order_by(order_by)
                .limit(limit))

        result = await session.execute(stmt)

        return result.scalars().all()

employee_repository = EmployeeRepository()