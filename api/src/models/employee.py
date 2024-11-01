from datetime import date
from typing import List, Optional

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
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

    acting_head_id: Mapped[int] = mapped_column(ForeignKey("employees.id", use_alter=True, ondelete="CASCADE"))
    acting_head: Mapped["Employee"] = relationship(back_populates="employees")

    employees: Mapped[List["Employee"]] = relationship(back_populates="employees")

class Sex(Base):
    __tablename__ = "sex"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(32), unique=True)

    employees: Mapped[List["Employee"]] = relationship(back_populates="employees")

class EmployeePosition(Base):
    __tablename__ = "employee_positions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    employees: Mapped[List["Employee"]] = relationship(back_populates="employees")

class EmploymentType(Base):
    __tablename__ = "employment_types"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    employees: Mapped[List["Employee"]] = relationship(back_populates="employees")

class Employee(Base):
    __tablename__ = "employees"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id", use_alter=True, ondelete="CASCADE"))
    country: Mapped[Country] = relationship(back_populates="countries")
    
    department_id: Mapped[Optional[int]] = mapped_column(ForeignKey("departments.id", use_alter=True, ondelete="CASCADE"))
    department: Mapped["Department"] = relationship(back_populates="departments")

    first_name: Mapped[str] = mapped_column(String(32))

    last_name: Mapped[Optional[str]] = mapped_column(String(64))

    middle_name: Mapped[Optional[str]] = mapped_column(String(32))
    
    sex_id: Mapped[int]

    login: Mapped[str] = mapped_column(String(32), unique=True)

    password: Mapped[str] = mapped_column(String(32))

    email: Mapped[Optional[str]] = mapped_column(String(64), unique=True)

    phone: Mapped[Optional[str]] = mapped_column(String(16), unique=True)

    employment_type_id: Mapped[int] = mapped_column(ForeignKey("employment_types.id", use_alter=True, ondelete="CASCADE"))
    employment_type: Mapped[EmploymentType] = relationship(back_populates="employment_types")

    created_at: Mapped[date] = mapped_column(Date, server_default=func.now())

    deleted_at: Mapped[Optional[date]] = mapped_column(Date)

    positions: Mapped["EmployeePosition"] = relationship(back_populates="employee_positions")

    business_trips: Mapped[List["BusinessTrip"]] = relationship(back_populates="business_trips")

    vacation: Mapped[List["Vacation"]] = relationship(back_populates="vacations")

class EmployeeEmployeePosition(Base):
    __tablename__ = "employee__employee_positions"

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", use_alter=True, ondelete="CASCADE"), 
                                             primary_key=True)
    position_id: Mapped[int] = mapped_column(ForeignKey("employee_positions.id", use_alter=True, ondelete="CASCADE"), 
                                             primary_key=True)

class BusinessTrip(Base):

    #TODO: сделать проверку дат

    __tablename__ = "business_trips"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="CASCADE"))
    employee: Mapped[Employee] = relationship(back_populates="employees")

    start_date: Mapped[date] = mapped_column(Date, server_default=func.now())

    end_date: Mapped[date] = mapped_column(Date)

    destionation_city: Mapped[str] = mapped_column(String(128))

    reason: Mapped[str] = mapped_column(String(256))

    deleted_at: Mapped[Optional[date]] = mapped_column(Date)

class VacationType(Base):
    __tablename__ = "vacation_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

class Vacation(Base):

    #TODO: сделать проверку дат

    __tablename__ = "vacations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))
    employee: Mapped[Employee] = relationship(back_populates="employees")

    start_date: Mapped[date] = mapped_column(Date, server_default=func.now())

    end_date: Mapped[date] = mapped_column(Date)

    reason: Mapped[str] = mapped_column(String(256))

    vacation_type_id: Mapped[int] = mapped_column(ForeignKey("vacation_types.id"))