from typing import List, Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (APIRouter, Depends, 
                     HTTPException, status,
                     Query)

from src.employee import crud
from src.employee.schemas import (Employee as EmployeeSchema, 
                                  CreateEmployee as CreateEmployeeSchema,
                                  UpdateEmployee as UpdateEmployeeSchema)
from src.models.employee import Employee
from src.database import session_dependency

router = APIRouter(prefix="/employee", tags=["employees"])

@router.get("", response_model=List[EmployeeSchema])
async def get_employees(limit: Annotated[int, Query(ge=1, le=1000)]=100,
                        session: AsyncSession=Depends(session_dependency)):
    return await crud.get_models(Employee, limit, session=session)


@router.post("", response_model=EmployeeSchema)
async def create_employee(data: CreateEmployeeSchema, 
                          session: AsyncSession = Depends(session_dependency)):
    return await crud.create_model(Employee, data, session)

@router.patch("/{employee_id}", status_code=204)
async def update_employee(employee_id: int,
                         data: UpdateEmployeeSchema,
                         session: AsyncSession = Depends(session_dependency)):
    result = await crud.update_model(Employee, employee_id, data, session)


@router.delete("/{employee_id}", status_code=204)
async def delete_employee(employee_id: int,
                         session: AsyncSession = Depends(session_dependency)):
    result = await crud.delete_model(Employee, employee_id, session)

@router.get("/{employee_id}", response_model=EmployeeSchema)
async def get_employee_by_id(employee_id: int, 
                             session: AsyncSession = Depends(session_dependency)):
    employee = await crud.get_model_by_id(Employee, employee_id, session=session)
    if employee is not None:
        return employee
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
    )