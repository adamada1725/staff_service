from fastapi import FastAPI
import uvicorn

from src.routers import employee

app = FastAPI()
app.include_router(employee.router)

if __name__=="__main__":
    uvicorn.run("src.main:app", reload=True)