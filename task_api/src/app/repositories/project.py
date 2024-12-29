from base.repositories import BaseRepository
from app.models import Project
from app.schemas.project import Project as ProjectSchema

project_repository = BaseRepository(Project, ProjectSchema)