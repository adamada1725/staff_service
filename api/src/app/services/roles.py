from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.repositories.roles import RoleRepository
from app.schemas.roles import CreateRole, Role

class RoleService:

    _repo = RoleRepository
    
    @classmethod
    async def save(cls, session: AsyncSession, schema: CreateRole):
        
        return await cls._repo.save(session, schema)

    @classmethod
    async def get_all(cls, session: AsyncSession):
        
        response = await cls._repo.get_all(session)
        
        return response

    @classmethod
    async def get_one(cls, session: AsyncSession, id: int):

        response = await cls._repo.get_one(session, id)

        return response
    
    @classmethod
    async def delete_one(cls, session: AsyncSession, id: int):
        
        await cls._repo.delete_one(session, id)
        
    @classmethod
    async def update_one(cls, session: AsyncSession, id: int, role_schema: CreateRole):
        
        await cls._repo.get_one(session, id)
        return await cls._repo.update_one(session, id, role_schema)
