from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PersonalInfo
from app.schemas.personal_info import CreatePersonalInfo
from base.repository import BaseRepository

class PersonalInfoRepository(BaseRepository):

    async def save(self, session: AsyncSession, schema: CreatePersonalInfo, employee_id):
        new_model = self.model(**schema.model_dump(), employee_id = employee_id)
        session.add(new_model)

        return new_model

personal_info_repository = PersonalInfoRepository(PersonalInfo)