from asyncio import current_task

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session

from config import settings

class Database():

    engine = create_async_engine(settings.db_url, echo=settings.POSTGRES_ECHO)

    session_factory = async_sessionmaker(engine,
                             autoflush=False,
                             autocommit=False,
                             expire_on_commit=False)

    @classmethod
    def get_scoped_session(cls):
        sess = async_scoped_session(
            session_factory = cls.session_factory,
            scopefunc = current_task
        )
        return sess

    @classmethod
    async def session_dependency(cls):
        sess = cls.get_scoped_session()
        try:
            yield sess
        except Exception:
            sess.rollback()
            raise
        finally:
            await sess.close()