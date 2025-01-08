import asyncio
import sys
import uvicorn

from fastapi import FastAPI

from app.routers import project, task, workspace

app = FastAPI()

routers = [project.router, task.router, workspace.router]
for r in routers:
    app.include_router(r)

async def main(argv):

    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=4000)

    

if __name__=="__main__":
    asyncio.run(main(sys.argv))