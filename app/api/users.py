from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import user_services

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user_endpoint(user:UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_services.create_user(db=db, user=user)