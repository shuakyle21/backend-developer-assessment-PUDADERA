from sqlalchemy import Column, Date, Integer, String
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    project_name = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
