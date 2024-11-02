from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.employee.schemas import CreateEmployee
from src.models.employee import Employee

async def get_employees(limit: int, session: AsyncSession) -> List[Employee]:
    stmt = select(Employee).order_by(Employee.id).limit(limit)
    result: Result = await session.execute(stmt)
    employees = result.scalars().all()
    return employees

async def get_employee_by_id(session: AsyncSession, employee_id: int) -> Optional[Employee]:
    stmt = select(Employee).where(Employee.id == employee_id)
    result: Result = await session.execute(stmt)
    employee = result.scalar_one_or_none()
    return employee

async def create_employee(session: AsyncSession, data: CreateEmployee) -> Employee:
    employee = Employee(**data.model_dump())
    session.add(employee)
    await session.commit()
    await session.refresh(employee)
    return employee