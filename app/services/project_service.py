from fastapi import HTTPException

from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectUpdate

VALID_STATUSES = {"Planning", "In Progress", "On Hold", "Completed"}
VALID_PRIORITIES = {"Low", "Medium", "High"}


class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def _validate(self, data: ProjectCreate | ProjectUpdate) -> None:
        if not data.client_name or not data.client_name.strip():
            raise HTTPException(status_code=422, detail="Client Name is required")

        if not data.project_name or not data.project_name.strip():
            raise HTTPException(status_code=422, detail="Project Name is required")

        if data.status not in VALID_STATUSES:
            raise HTTPException(status_code=422, detail=f"Status must be one of {sorted(VALID_STATUSES)}")

        if data.priority not in VALID_PRIORITIES:
            raise HTTPException(status_code=422, detail=f"Priority must be one of {sorted(VALID_PRIORITIES)}")

        if data.due_date < data.start_date:
            raise HTTPException(status_code=422, detail="Due Date cannot be earlier than Start Date")

    def get_all(self) -> list[Project]:
        return self.repository.get_all()

    def get_by_id(self, project_id: int) -> Project:
        project = self.repository.get_by_id(project_id)
        if project is None:
            raise HTTPException(status_code=404, detail=f"Project {project_id} not found")
        return project

    def create(self, data: ProjectCreate) -> Project:
        self._validate(data)
        project = Project(**data.model_dump())
        return self.repository.create(project)

    def update(self, project_id: int, data: ProjectUpdate) -> Project:
        self._validate(data)
        project = self.get_by_id(project_id)

        for field, value in data.model_dump().items():
            setattr(project, field, value)

        return self.repository.update(project)

    def delete(self, project_id: int) -> None:
        project = self.get_by_id(project_id)
        self.repository.delete(project)
