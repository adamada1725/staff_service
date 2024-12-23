from asyncio import current_task

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker, 
                                    async_scoped_session)
from sqlalchemy.orm import DeclarativeBase

from config import settings

engine = create_async_engine(
    url=settings.db_url,
    echo=settings.POSTGRES_ECHO
    )

session_factory = async_sessionmaker(engine,
                             autoflush=False,
                             autocommit=False,
                             expire_on_commit=False)

def get_scoped_session():
    sess = async_scoped_session(
        session_factory = session_factory,
        scopefunc = current_task
    )
    return sess

async def session_dependency():
    sess = get_scoped_session()
    try:
        yield sess
    except Exception:
        sess.rollback()
        raise
    finally:
        await sess.close()

class Base(DeclarativeBase):
    pass


async def truncate_all():
    async with engine.begin() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            await conn.execute(text(f"TRUNCATE TABLE {table.name} RESTART IDENTITY CASCADE"))