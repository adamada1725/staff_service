from typing import List, TypeVar, Type, Optional
from abc import ABC, abstractmethod

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Base
from base.schemas import BaseInstance

M = TypeVar("M", bound=Base)
S = TypeVar("S", bound=BaseInstance)

class AbstractRepository(ABC):

    @abstractmethod
    async def find_all(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def save(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def save_all(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def delete_all(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def delete_by_id(self, **kwargs):
        raise NotImplementedError



class BaseRepository(AbstractRepository):
    
    def __init__(self, model: Type[M], schemas: Type[S]):
        self.model = model
        self.schemas: Type[S] = schemas

    async def find_all(self, 
                       session: AsyncSession,
                       order_by: str = "id", 
                       limit: int = 100,
                       unique: bool = False,
                       **filters) -> Optional[List[M]]:

        stmt = (select(self.model)
                .filter_by(**filters)
                .order_by(order_by)
                .limit(limit))

        result = await session.execute(stmt)

        return result.scalars().all()

    async def find_by_id(self, 
                         session: AsyncSession, 
                         id: int):

        return await session.get_one(self.model, id)

    async def save(self, session: AsyncSession, schema):
        new_model = self.model(**schema.model_dump())
        session.add(new_model)
        await session.commit()
        await session.refresh(new_model)

        return new_model

    async def save_all(self, session: AsyncSession):
        ...

    async def delete_all(self, session: AsyncSession, filters: dict):
        ...

    async def delete_by_id(self, session: AsyncSession, id: int):
        
        model = await session.get_one(self.model, id)
        await session.delete(model)
        await session.commit()
        return model
    
    async def update_by_id(self, session: AsyncSession, id: int, schema):

        stmt = update(self.model).where(self.model.id==id).values(**schema.model_dump())
        
        await session.execute(stmt)
        await session.commit()
        model = await session.get_one(self.model, id)
        return model
