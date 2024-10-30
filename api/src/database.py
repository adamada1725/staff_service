from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr

from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
    )

session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass