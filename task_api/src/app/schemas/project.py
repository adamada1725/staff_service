from base.schemas import BaseInstance

Project = BaseInstance

Project.Base = Project.Base.with_fields(workspace_id=(int, ...))