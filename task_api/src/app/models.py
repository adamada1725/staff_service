from datetime import datetime
from typing import List, Optional

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass

class BaseInstance(Base):
    
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str] = mapped_column(String, nullable=True)

    created_by: Mapped[int] = mapped_column(Integer)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

class Workspace(BaseInstance):

    __tablename__ = "workspaces"

    projects: Mapped[List["Project"]] = relationship("Project", backref="workspace")

class Project(BaseInstance):

    __tablename__ = "projects"

    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)

    tasks: Mapped[List["Task"]] = relationship("Task", backref="project")

class Task(BaseInstance):

    __tablename__ = "tasks"

    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)

    deadline: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    __table_args__ = (
        CheckConstraint("created_at < deadline"),
    )