from pydantic import BaseModel
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    description: str | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: str
    created_at: datetime
    updated_at: datetime | None = None
    owner_id: str
