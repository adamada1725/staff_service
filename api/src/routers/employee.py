from typing import List, Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (APIRouter, Depends, 
                     HTTPException, status,
                     Query)

from src.employee import crud
from src.employee.schemas import CreateEmployee, Employee
from src.database import session_dependency

router = APIRouter(prefix="/employee", tags=["employees"])

@router.get("", response_model=List[Employee])
async def get_employees(limit: Annotated[int, Query(ge=1, le=1000)]=100,
                        session: AsyncSession=Depends(session_dependency)):
    return await crud.get_employees(limit, session=session)


@router.post("", response_model=Employee)
async def create_employee(employee: CreateEmployee, 
                          session: AsyncSession = Depends(session_dependency)):
    return await crud.create_employee(data=employee, session=session)


@router.get("/{employee_id}", response_model=Employee)
async def get_employees(employee_id: int, 
                        session: AsyncSession = Depends(session_dependency)):
    employee = await crud.get_employee_by_id(session=session, employee_id=employee_id)
    if employee is not None:
        return employee
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
    )