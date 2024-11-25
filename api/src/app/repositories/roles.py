from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from base.repository import AbstractRepository
from app.models import Role
from app.schemas.roles import CreateRole

class RoleRepository(AbstractRepository):

    @classmethod
    async def save(cls, session: AsyncSession, schema: CreateRole) -> Role:

        new_role = Role(**schema.model_dump())

        session.add(new_role)
        await session.commit()
        await session.refresh(new_role)

        return new_role
    
    @classmethod
    async def get_one(cls, session: AsyncSession, id: int) -> Role:

        return await session.get_one(Role, id)
    
    @classmethod
    async def get_all(cls, session: AsyncSession) -> Sequence[Role]:

        return (await session.execute(select(Role))).scalars().all()
    
    @classmethod
    async def delete_one(cls, session: AsyncSession, id: int):
        
        role = await session.get_one(Role, id)
        await session.delete(role)
        await session.commit()
        
    @classmethod
    async def update_one(cls, session: AsyncSession, id: int, role_schema: CreateRole):
        
        stmt = update(Role).where(Role.id==id).values(**role_schema.model_dump())
        
        result = await session.execute(stmt)
        await session.commit()