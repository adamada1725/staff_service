from base.repositories import BaseRepository
from app.models import Workspace
from app.schemas.workspace import Workspace as WorkspaceSchemas

workspace_repository = BaseRepository(Workspace, WorkspaceSchemas)