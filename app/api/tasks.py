from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.database import get_db
from app.db.models import User
from app.schemas.task import TaskCreate, TaskResponse
from app.api.deps import get_current_user
from app.services import task_service

router = APIRouter()

@router.post("/", response_model=TaskResponse)
async def create_new_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await task_service.create_task(db=db, task=task, user_id=current_user.id)

@router.get("/", response_model=List[TaskResponse])
async def read_tasks(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await task_service.get_user_tasks(db=db, user_id=current_user.id)