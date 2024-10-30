from datetime import date

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base

class Country(Base):
    __tablename__ = "country"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    title: Mapped[str] = mapped_column(String(32), unique=True)
    
    employees: Mapped["Employee"] = relationship(back_populates="employee")

class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    acting_head_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    acting_head: Mapped["Employee"] = relationship(back_populates="employee")

    employees: Mapped[list["Employee"]] = relationship(back_populates="employee")

class Sex(Base):
    __tablename__ = "sex"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(32), unique=True)

    employees: Mapped[list["Employee"]] = relationship(back_populates="employee")

class Position(Base):
    __tablename__ = "position"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    employees: Mapped[list["Employee"]] = relationship(back_populates="employee")

class Employment_type(Base):
    __tablename__ = "employment_type"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

    employees: Mapped[list["Employee"]] = relationship(back_populates="employee")

class Employee(Base):
    __tablename__ = "employee"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    country_id: Mapped[int] = mapped_column(ForeignKey(Country.id))
    country: Mapped[Country] = relationship(back_populates=Country)
    
    department_id: Mapped[int|None] = mapped_column(ForeignKey(Department.id))
    department: Mapped[Department] = relationship(back_populates=Department)

    first_name: Mapped[str] = mapped_column(String(32))

    last_name: Mapped[str|None] = mapped_column(String(64))

    middle_name: Mapped[str|None] = mapped_column(String(32))
    
    sex_id: Mapped[int]

    login: Mapped[str] = mapped_column(String(32), unique=True)

    password: Mapped[str] = mapped_column(String(32))

    email: Mapped[str|None] = mapped_column(String(64), unique=True)

    phone: Mapped[str|None] = mapped_column(String(16), unique=True)

    employment_type_id: Mapped[int] = mapped_column(ForeignKey(Employment_type.id))
    employment_type: Mapped[Employment_type] = relationship(back_populates=Employment_type)

    created_at: Mapped[date] = mapped_column(Date, server_default=func.now())

    deleted_at: Mapped[date|None] = mapped_column(Date)

    positions: Mapped["EmployeePosition"] = relationship(back_populates="EmployeePosition")

    business_trips: Mapped[list["BusinessTrip"]] = relationship(back_populates="BusinessTrip")

    vacation: Mapped[list["Vacation"]] = relationship(back_populates="Vacation")

class EmployeePosition(Base):
    __tablename__ = "employee_position"

    employee_id: Mapped[int] = mapped_column(ForeignKey(Employee.id), primary_key=True)
    position_id: Mapped[int] = mapped_column(ForeignKey(Position.id), primary_key=True)

class BusinessTrip(Base):
    __tablename__ = "business_trip"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    employee_id: Mapped[int] = mapped_column(ForeignKey(Employee.id))
    employee: Mapped[Employee] = relationship(back_populates="Employee.id")

    start_date: Mapped[date] = mapped_column(Date, server_default=func.now())

    end_date: Mapped[date] = mapped_column(Date)

    destionation_city: Mapped[str] = mapped_column(String(128))

    resaon: Mapped[str] = mapped_column(String(256))

    deleted_at: Mapped[date|None] = mapped_column(Date)

class VacationType(Base):
    __tablename__ = "vacation_type"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(64), unique=True)

class Vacation(Base):
    __tablename__ = "vacation"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    employee_id: Mapped[int] = mapped_column(ForeignKey(Employee.id))
    employee: Mapped[Employee] = relationship(back_populates="Employee.id")

    start_date: Mapped[date] = mapped_column(Date, server_default=func.now())

    end_date: Mapped[date] = mapped_column(Date)

    resaon: Mapped[str] = mapped_column(String(256))

    vacation_type_id: Mapped[int] = mapped_column(ForeignKey(VacationType.id))