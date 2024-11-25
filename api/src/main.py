import sys
import asyncio

from fastapi import FastAPI
import uvicorn

from base.database import truncate_all

from app.routers.roles import router as roles_router
from app.routers.users import users_router
from app.routers.departments import departments_router
from app.routers.employment_types import employment_types_router
from app.routers.position_types import position_type_router
from app.routers.vacation_types import vacation_type_router
from app.routers.employees import employees_router
from app.routers.vacations import vacations_router
from app.routers.business_trips import business_trips_router


app = FastAPI()

app.include_router(roles_router)
app.include_router(users_router)
app.include_router(departments_router)
app.include_router(employment_types_router)
app.include_router(position_type_router)
app.include_router(vacation_type_router)
app.include_router(employees_router)
app.include_router(vacations_router)
app.include_router(business_trips_router)

if __name__=="__main__":

    if "-t" in sys.argv or "--truncate" in sys.argv:
        asyncio.run(truncate_all())
    uvicorn.run("main:app", reload=True)