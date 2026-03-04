from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.db.database import get_db
from app.db.models import User
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
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

@router.put("/{task_id}", response_model=TaskResponse)
async def update_existing_task(
    task_id: int,
    task_update: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_task = await task_service.update_task(
        db= db, task_id= task_id, user_id= current_user.id, task_data= task_update 
    )
    
    if not updated_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    return updated_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = await task_service.delete_task(db= db, task_id= task_id, user_id= current_user.id)
    
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return None

@router.get("/", response_model=List[TaskResponse])
async def read_tasks(
    skip: int = 0,
    limit: int = 100,
    is_completed: Optional[bool] = None,
    category_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await task_service.get_user_tasks(
        db=db,
        user_id=current_user.id,
        skip=skip,
        limit=limit,
        is_completed=is_completed,
        category_id=category_id
    )