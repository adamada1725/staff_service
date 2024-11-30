from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models import User
from base.repository import BaseRepository

class UserRepository(BaseRepository):

    def __init__(self):
        self.model = User

    async def find_all(self, 
                       session: AsyncSession, 
                       order_by: str = "id", 
                       limit: int = 100, 
                       unique: bool = False, 
                       **filters):
        
        stmt = (select(self.model)
                .filter_by(**filters)
                .order_by(order_by)
                .limit(limit))

        result = (await session.execute(stmt)).scalars().all()

        for o in result:
            del o.__dict__["password"]

        return result

    async def find_by_id(self, 
                         session: AsyncSession, 
                         id: int):
        
        result = await session.get_one(self.model, id)
        del result.__dict__["password"]
        return result
        
        


user_repository = UserRepository()