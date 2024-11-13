from typing import List, TypeVar, Type, Optional
from abc import ABC, abstractmethod


from domain.departments.schemas import Department as DepartmentSchema

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from base.database import Base

M = TypeVar("M", bound=Base)

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
    
    def __init__(self, model: Type[M]):
        self.model = model

    async def find_all(self, 
                       session: AsyncSession,
                       order_by: str = "id", 
                       limit: int = 100,
                       **filters) -> Optional[List[M]]:

        stmt = (select(self.model)
                .filter_by(**filters)
                .order_by(order_by)
                .limit(limit))

        result = await session.execute(stmt)

        result = result.fetchall()

        res = result[0][0]

        res = DepartmentSchema.model_validate(res).model_dump_json(exclude=DepartmentSchema.title)

        return res

    async def find_by_id(self, 
                         session: AsyncSession, 
                         id: int):
        ...

    async def save(self, session: AsyncSession):
        ...

    async def save_all(self, session: AsyncSession):
        ...

    async def delete_all(self, session: AsyncSession, filters: dict):
        ...

    async def delete_by_id(self, session: AsyncSession, id: int):
        ...