from datetime import date

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from src.database import Base

class Country(Base):
    __tablename__ = "countries"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    title: Mapped[str] = mapped_column(String(32), unique=True)
    
    employees: Mapped["Employee"] = relationship(back_populates="employee")

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    acting_head_id: Mapped[int] = mapped_column(ForeignKey("employees.id", use_alter=True, ondelete="CASCADE"))
    acting_head: Mapped["Employee"] = relationship(back_populates="employees")

    employees: Mapped[list["Employee"]] = relationship(back_populates="employees")

class Sex(Base):
    __tablename__ = "sex"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(32), unique=True)

    employees: Mapped[list["Employee"]] = relationship(back_populates="employee")

class Position(Base):
    __tablename__ = "positions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    employees: Mapped[list["Employee"]] = relationship(back_populates="employee")

class Employment_type(Base):
    __tablename__ = "employment_types"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    employees: Mapped[list["Employee"]] = relationship(back_populates="employee")

class Employee(Base):
    __tablename__ = "employees"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    country_id: Mapped[int] = mapped_column(ForeignKey(Country.id, use_alter=True, ondelete="CASCADE"))
    country: Mapped[Country] = relationship(back_populates=Country)
    
    department_id: Mapped[int|None] = mapped_column(ForeignKey("departments.id", use_alter=True, ondelete="CASCADE"))
    department: Mapped["Department"] = relationship(back_populates="departments")

    first_name: Mapped[str] = mapped_column(String(32))

    last_name: Mapped[str|None] = mapped_column(String(64))

    middle_name: Mapped[str|None] = mapped_column(String(32))
    
    sex_id: Mapped[int]

    login: Mapped[str] = mapped_column(String(32), unique=True)

    password: Mapped[str] = mapped_column(String(32))

    email: Mapped[str|None] = mapped_column(String(64), unique=True)

    phone: Mapped[str|None] = mapped_column(String(16), unique=True)

    employment_type_id: Mapped[int] = mapped_column(ForeignKey(Employment_type.id, use_alter=True, ondelete="CASCADE"))
    employment_type: Mapped[Employment_type] = relationship(back_populates=Employment_type)

    created_at: Mapped[date] = mapped_column(Date, server_default=func.now())

    deleted_at: Mapped[date|None] = mapped_column(Date)

    positions: Mapped["EmployeePosition"] = relationship(back_populates="EmployeePosition")

    business_trips: Mapped[list["BusinessTrip"]] = relationship(back_populates="BusinessTrip")

    vacation: Mapped[list["Vacation"]] = relationship(back_populates="Vacation")

class EmployeePosition(Base):
    __tablename__ = "employee_positions"

    employee_id: Mapped[int] = mapped_column(ForeignKey(Employee.id, ondelete="CASCADE"), primary_key=True)
    position_id: Mapped[int] = mapped_column(ForeignKey(Position.id, ondelete="CASCADE"), primary_key=True)

class BusinessTrip(Base):

    #TODO: сделать проверку дат

    __tablename__ = "business_trips"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    employee_id: Mapped[int] = mapped_column(ForeignKey(Employee.id, ondelete="CASCADE"))
    employee: Mapped[Employee] = relationship(back_populates="employee.id")

    start_date: Mapped[date] = mapped_column(Date, server_default=func.now())

    end_date: Mapped[date] = mapped_column(Date)

    destionation_city: Mapped[str] = mapped_column(String(128))

    resaon: Mapped[str] = mapped_column(String(256))

    deleted_at: Mapped[date|None] = mapped_column(Date)

class VacationType(Base):
    __tablename__ = "vacation_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

class Vacation(Base):

    #TODO: сделать проверку дат

    __tablename__ = "vacations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    employee_id: Mapped[int] = mapped_column(ForeignKey(Employee.id))
    employee: Mapped[Employee] = relationship(back_populates="Employee.id")

    start_date: Mapped[date] = mapped_column(Date, server_default=func.now())

    end_date: Mapped[date] = mapped_column(Date)

    resaon: Mapped[str] = mapped_column(String(256))

    vacation_type_id: Mapped[int] = mapped_column(ForeignKey(VacationType.id))