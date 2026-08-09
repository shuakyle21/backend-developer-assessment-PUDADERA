from pydantic import BaseModel
from datetime import date as Date

class ProjectBase(BaseModel):
    client_name: str
    project_name: str
    description: str | None = None
    status: str
    priority: str
    start_date: Date
    due_date: Date

class ProjectCreate(ProjectBase):
    pass
class ProjectUpdate(ProjectBase):
    pass
class ProjectOut(ProjectBase):
    id: int
    model_config = {
        "from_attributes": True,
    }