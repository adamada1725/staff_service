from fastapi import APIRouter

from base.routers import BaseRouterFactory
from app.repositories.project import project_repository

router = APIRouter(prefix="/projects")

endpoints = BaseRouterFactory(router, project_repository)