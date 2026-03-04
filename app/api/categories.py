from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.models import User
from app.db.database import get_db
from app.api.deps import get_current_user
from app.schemas.category import CategoryCreate, CategoryResponse
from app.services import category_service

router = APIRouter()

@router.post("/", response_model=CategoryResponse)
async def create_new_category(
    category: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await category_service.create_category(db=db, category=category)

@router.get("/", response_model=List[CategoryResponse])
async def read_categories(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await category_service.get_categories(db=db)