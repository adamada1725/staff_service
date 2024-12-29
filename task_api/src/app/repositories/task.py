from base.repositories import BaseRepository
from app.models import Task
from app.schemas.task import Task as TaskSchema

task_repository = BaseRepository(Task, TaskSchema)