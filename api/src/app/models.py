from datetime import date, datetime
from typing import Optional
from sqlalchemy import (
    CheckConstraint, String, Integer, Date, DateTime, ForeignKey, Boolean, func
)
from sqlalchemy.orm import mapped_column, relationship, Mapped, declared_attr

from base.database import Base

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32), nullable=False)
    token: Mapped[str] = mapped_column(String(100), nullable=False)

    users: Mapped[list["User"]] = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE", use_alter=True))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    role: Mapped["Role"] = relationship("Role", back_populates="users")
    employee: Mapped["Employee"] = relationship("Employee", back_populates="user", uselist=False)


class Employee(Base):
    __tablename__ = "employees"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE", use_alter=True), primary_key=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id", ondelete="CASCADE", use_alter=True), nullable=True)
    employment_type_id: Mapped[int] = mapped_column(ForeignKey("employment_types.id", ondelete="CASCADE", use_alter=True))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="employee")
    #department: Mapped["Department"] = relationship("Department", back_populates="employees")
    employment_type: Mapped["EmploymentType"] = relationship("EmploymentType", back_populates="employees")
    personal_info: Mapped["PersonalInfo"] = relationship("PersonalInfo", back_populates="employee", uselist=False)
    contact_info: Mapped["ContactInfo"] = relationship("ContactInfo", back_populates="employee", uselist=False)
    #positions: Mapped[list["EmployeePosition"]] = relationship("EmployeePosition", back_populates="employee")
    business_trips: Mapped[list["BusinessTrip"]] = relationship("BusinessTrip", back_populates="employee")
    vacations: Mapped[list["Vacation"]] = relationship("Vacation", back_populates="employee")


class Country(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    


class PersonalInfo(Base):
    __tablename__ = "personal_info"

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.user_id", ondelete="CASCADE", use_alter=True), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(64), nullable=False)
    last_name: Mapped[str] = mapped_column(String(64), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(64))
    birthdate: Mapped[Date] = mapped_column(Date)
    sex: Mapped[bool] = mapped_column(Boolean)
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id", ondelete="CASCADE", use_alter=True), nullable=True)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="personal_info")


class ContactInfo(Base):
    __tablename__ = "contact_info"

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.user_id", ondelete="CASCADE", use_alter=True), primary_key=True)
    email: Mapped[str] = mapped_column(String(64), unique=True)
    phone: Mapped[str] = mapped_column(String(16), unique=True)
    tg_id: Mapped[str] = mapped_column(String(64), unique=True)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="contact_info")


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    acting_head_id: Mapped[int] = mapped_column(ForeignKey("employees.user_id", ondelete="CASCADE", use_alter=True))

    #employees: Mapped[list["Employee"]] = relationship("Employee", back_populates="department")


class EmploymentType(Base):
    __tablename__ = "employment_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False)

    employees: Mapped[list["Employee"]] = relationship("Employee", back_populates="employment_type")


class PositionType(Base):
    __tablename__ = "position_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False)


class EmployeePositionType(Base):
    __tablename__ = "employees__position_types"

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.user_id", ondelete="CASCADE"), primary_key=True)
    position_id: Mapped[int] = mapped_column(ForeignKey("position_types.id", ondelete="CASCADE"), primary_key=True)


class EmployeeTrip(Base):
    __abstract__ = True

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.user_id", ondelete="CASCADE", use_alter=True))
    
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
    city: Mapped[str] = mapped_column(String(32))

    employee: Mapped["Employee"] = relationship("Employee", back_populates="business_trips")


class VacationType(Base):
    __tablename__ = "vacation_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False)


class Vacation(EmployeeTrip):
    __tablename__ = "vacations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vacation_type_id: Mapped[int] = mapped_column(ForeignKey("vacation_types.id", ondelete="CASCADE", use_alter=True))

    employee: Mapped["Employee"] = relationship("Employee", back_populates="vacations")
    vacation_type: Mapped["VacationType"] = relationship("VacationType")
