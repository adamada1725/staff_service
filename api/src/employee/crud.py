from typing import List, Optional, TypeVar, Type

from pydantic import BaseModel
from sqlalchemy import select, update, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Response, status

from src.employee.schemas import CreateEmployee
from src.models.employee import Employee
from src.database import Base

M = TypeVar("M", bound=Base)
S = TypeVar("S", bound=BaseModel)

async def get_models(model: Type[M], limit: int, session: AsyncSession) -> List[M]:
    stmt = select(model).limit(limit)
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_model_by_id(model: Type[M], id: int, session: AsyncSession) -> M:
    result = await session.get(model, id)
    return result

async def create_model(model: Type[M], data: Type[S], session: AsyncSession) -> M:
    parsed_model = model(**data.model_dump())
    session.add(parsed_model)
    await session.commit()
    await session.refresh(parsed_model)
    return parsed_model

async def update_model(model: Type[M], id: int, data: Type[S], session: AsyncSession) -> None:
    stmt = update(model).where(model.id == id).values(**data.model_dump())
    result = await session.execute(stmt)
    await session.commit()
    return

async def delete_model(model: Type[M], id: int, session: AsyncSession) -> None:
    stmt = delete(model).where(model.id == id)
    result = await session.execute(stmt)
    await session.commit()
    return