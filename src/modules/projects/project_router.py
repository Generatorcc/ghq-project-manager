from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database.database import SessionLocal
from src.modules.projects.project_model import Project
from src.modules.projects.project_schema import ProjectCreate, ProjectOut
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=ProjectOut)
async def create_project(project: ProjectCreate, db: AsyncSession = Depends(SessionLocal)):
    db_project = Project(name=project.name, description=project.description, owner_id="owner-uuid-placeholder", created_at=datetime.utcnow(), updated_at=None)
    db.add(db_project)
    await db.commit()
    await db.refresh(db_project)
    return db_project

@router.get("/", response_model=list[ProjectOut])
async def list_projects(db: AsyncSession = Depends(SessionLocal)):
    result = await db.execute(select(Project))
    return result.scalars().all()
