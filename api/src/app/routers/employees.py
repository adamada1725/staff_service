from typing import Annotated
from fastapi import Depends, Path, Query
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from base.database import session_dependency
from app.schemas.employees import CreateEmployee, UpdateEmployee
from app.services.employees import EmployeeService
from base.utils.router_exception_handler import handle_exceptions

employees_router = APIRouter(prefix="/employees", tags=["employees"])

SessionDependency = Annotated[AsyncSession, Depends(session_dependency)]


@employees_router.get("")
@handle_exceptions
async def get_employees(session: SessionDependency, 
                        full: Annotated[bool, Query()] = True):

    return await EmployeeService.get_all(session, full)

@employees_router.get("/{employee_id}")
@handle_exceptions
async def get_one_employee(employee_id: Annotated[int, Path(ge=1)],
                           session: SessionDependency):

    return await EmployeeService.get_one(session, employee_id)

@employees_router.post("")
@handle_exceptions
async def create_employee(employee_schema: CreateEmployee,
                          session: SessionDependency):
    
    return await EmployeeService.save(session, employee_schema)

@employees_router.delete("/{employee_id}")
@handle_exceptions
async def delete_employee(employee_id: Annotated[int, Path()],
                          session: SessionDependency):
    
    await EmployeeService.delete_one(session, employee_id)

@employees_router.patch("/{employee_id}")
@handle_exceptions
async def update_employee(employee_id: Annotated[int, Path()],
                          schema: UpdateEmployee,
                          session: SessionDependency):
    
    await EmployeeService.update_one(session, employee_id, schema)