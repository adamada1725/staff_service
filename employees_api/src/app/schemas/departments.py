from base.schema import BaseSchema


class CreateDepartment(BaseSchema):

    title: str

    acting_head_id: int

class DeaprtmentSchema(CreateDepartment):

    id: int

class UpdateDepartment(DeaprtmentSchema):

    pass