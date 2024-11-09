from datetime import date
from typing import List, Optional

from sqlalchemy import String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from sqlalchemy.sql import func

from src.database import Base

class Country(Base):
    __tablename__ = "countries"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    title: Mapped[str] = mapped_column(String(32), unique=True)

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    employees: Mapped[List["Employee"]] = relationship("Employee")

class Sex(Base):
    __tablename__ = "sex"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(32), unique=True)

    employees: Mapped[List["Employee"]] = relationship("Employee")

class EmployeePosition(Base):
    __tablename__ = "employee_positions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

class EmploymentType(Base):
    __tablename__ = "employment_types"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    employees: Mapped[List["Employee"]] = relationship("Employee")

class Employee(Base):
    __tablename__ = "employees"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id", use_alter=True, ondelete="CASCADE"))
    country: Mapped[Country] = relationship("Country")
    
    department_id: Mapped[Optional[int]] = mapped_column(ForeignKey("departments.id", use_alter=True, ondelete="CASCADE"))
    department: Mapped["Department"] = relationship("Department")

    first_name: Mapped[str] = mapped_column(String(32))

    last_name: Mapped[Optional[str]] = mapped_column(String(64))

    middle_name: Mapped[Optional[str]] = mapped_column(String(32))
    
    sex_id: Mapped[int] = mapped_column(ForeignKey("sex.id", use_alter=True, ondelete="CASCADE"))

    login: Mapped[str] = mapped_column(String(32), unique=True)

    password: Mapped[str] = mapped_column(String(100))

    email: Mapped[Optional[str]] = mapped_column(String(64), unique=True)

    phone: Mapped[Optional[str]] = mapped_column(String(16), unique=True)

    employment_type_id: Mapped[int] = mapped_column(ForeignKey("employment_types.id", use_alter=True, ondelete="CASCADE"))
    employment_type: Mapped[EmploymentType] = relationship("EmploymentType")

    created_at: Mapped[date] = mapped_column(Date, server_default=func.now())

    deleted_at: Mapped[Optional[date]] = mapped_column(Date)

    positions: Mapped[List["EmployeePosition"]] = relationship("EmployeeEmployeePosition")

    business_trips: Mapped[List["BusinessTrip"]] = relationship("BusinessTrip")

    vacation: Mapped[List["Vacation"]] = relationship("Vacation")

class EmployeeEmployeePosition(Base):
    __tablename__ = "employee__employee_positions"

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", use_alter=True, ondelete="CASCADE"), 
                                             primary_key=True)
    position_id: Mapped[int] = mapped_column(ForeignKey("employee_positions.id", use_alter=True, ondelete="CASCADE"), 
                                             primary_key=True)

#abstract
class EmployeeTrip(Base):
    __abstract__ = True

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="CASCADE"))
    
    @declared_attr
    def employee(cls) -> Mapped[Employee]:
        return relationship("Employee")

    start_date: Mapped[date] = mapped_column(Date, server_default=func.now())

    end_date: Mapped[date] = mapped_column(Date)

    reason: Mapped[str] = mapped_column(String(256))

    deleted_at: Mapped[Optional[date]] = mapped_column(Date)
    
    __table_args__ = (
        CheckConstraint("start_date <= end_date"),
    )

class BusinessTrip(EmployeeTrip):

    __tablename__ = "business_trips"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    destionation_city: Mapped[str] = mapped_column(String(128))

class VacationType(Base):
    __tablename__ = "vacation_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

class Vacation(EmployeeTrip):

    __tablename__ = "vacations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    vacation_type_id: Mapped[int] = mapped_column(ForeignKey("vacation_types.id"))