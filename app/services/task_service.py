from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Task
from app.schemas.task import TaskCreate, TaskUpdate

async def create_task(db: AsyncSession, task: TaskCreate, user_id: int):
    db_task = Task(**task.model_dump(), owner_id=user_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_user_tasks(db: AsyncSession, user_id: int):
    result = await db.execute(select(Task).where(Task.owner_id==user_id))
    return result.scalars().all()

async def get_task_by_id(db: AsyncSession, task_id: int, user_id: int):
    result = await db.execute(select(Task).where(Task.id==task_id, Task.owner_id==user_id))
    return result.scalars().first()

async def update_task(db: AsyncSession, task_id: int, user_id: int, task_data: TaskUpdate):
    db_task = await get_task_by_id(db, task_id, user_id)
    if not db_task:
        return None
    
    update_data = task_data.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_task, key, value)
        
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def delete_task(db: AsyncSession, task_id: int, user_id: int):
    db_task = await get_task_by_id(db, task_id, user_id)
    if not db_task:
        return None
    
    await db.delete(db_task)
    await db.commit()
    return True