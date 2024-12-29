from fastapi import APIRouter

from base.routers import BaseRouterFactory
from app.repositories.task import task_repository

router = APIRouter(prefix="/tasks")

endpoints = BaseRouterFactory(router, task_repository)