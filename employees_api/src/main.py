import sys
import asyncio

from fastapi import FastAPI
import uvicorn

from base.database import truncate_all
from base.seeders.seeders import BaseSeeder
from base.utils.security import RootDependency

from app.routers.countries import router as country_router
from app.routers.roles import router as roles_router
from app.routers.users import users_router
from app.routers.departments import departments_router
from app.routers.employment_types import employment_types_router
from app.routers.position_types import position_type_router
from app.routers.vacation_types import vacation_type_router
from app.routers.employees import employees_router
from app.routers.vacations import vacations_router
from app.routers.business_trips import business_trips_router

app = FastAPI(dependencies=[RootDependency])

app.include_router(roles_router)
app.include_router(users_router)
app.include_router(departments_router)
app.include_router(employment_types_router)
app.include_router(position_type_router)
app.include_router(vacation_type_router)
app.include_router(employees_router)
app.include_router(vacations_router)
app.include_router(business_trips_router)
app.include_router(country_router)

async def main(argv):

    if "-t" in argv or "--truncate" in sys.argv:
        await truncate_all()

    if "-s" in argv or "--seed" in sys.argv:
        await BaseSeeder.seed()

    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=6542)

    

if __name__=="__main__":
    asyncio.run(main(sys.argv))