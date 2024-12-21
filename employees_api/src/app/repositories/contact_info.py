from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ContactInfo
from app.schemas.contact_info import CreateConctactInfo
from base.repository import BaseRepository

class ContactInfoRepository(BaseRepository):

    async def save(self, session: AsyncSession, schema: CreateConctactInfo, employee_id):
        new_model = self.model(**schema.model_dump(), employee_id = employee_id)
        session.add(new_model)

        return new_model

contact_info_repository = ContactInfoRepository(ContactInfo)