from abc import ABC
import json
from typing import Dict, List
import pathlib

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from base.database import Base, get_scoped_session

class AbstractSeeder(ABC):
    pass

class BaseSeeder(AbstractSeeder):

    base = Base

    _seeder_JSON_file = "seeders_base.json"
    _dir = str(pathlib.Path(__file__).parent.resolve())
    _seeder_JSON_path = f"{_dir}\\{_seeder_JSON_file}"

    @classmethod
    def _parse_seeder_file(cls, path: str) -> Dict[str, List[Dict]]:
        
        with open(path, encoding="UTF8") as f:
            return json.loads(f.read())
    
    @classmethod
    async def seed(cls) -> None:

        session = get_scoped_session()

        seeder_dict = cls._parse_seeder_file(cls._seeder_JSON_path)

        for table, values in seeder_dict.items():
            stmt = cls.base.metadata.tables[table].insert().values(values)
            await session.execute(stmt)
        
        await session.commit()
