from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

engine = create_async_engine(
    url=settings.db_url,
    echo=settings.ECHO
    )

session = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass