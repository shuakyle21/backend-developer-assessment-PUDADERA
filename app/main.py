from fastapi import FastAPI

from app.controllers.projects import router as projects_router
from app.database import Base, engine
from app.models.project import Project  # noqa: F401 (needed so Base knows about the table)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Client Project Tracker API")

app.include_router(projects_router)
