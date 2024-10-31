from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
    )

session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass