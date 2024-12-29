from fastapi import APIRouter

from base.routers import BaseRouterFactory
from app.repositories.workspace import workspace_repository

router = APIRouter(prefix="/workspaces")

endpoints = BaseRouterFactory(router, workspace_repository)