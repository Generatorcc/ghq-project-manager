from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database.database import SessionLocal
from src.modules.users.user_model import User
from src.modules.users.user_schema import UserCreate, UserOut, UserLogin

router = APIRouter()

@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: AsyncSession = Depends(SessionLocal)):
    db_user = User(email=user.email, full_name=user.full_name, hashed_password=user.password, is_active=True, is_superuser=False)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[UserOut])
async def list_users(db: AsyncSession = Depends(SessionLocal)):
    result = await db.execute(select(User))
    return result.scalars().all()
