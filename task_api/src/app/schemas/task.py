from base.schemas import BaseInstance

Task = BaseInstance

Task.Base = Task.Base.with_fields(project_id=(int, ...))