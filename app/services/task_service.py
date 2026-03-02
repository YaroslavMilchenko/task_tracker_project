from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Task
from app.schemas.task import TaskCreate

async def create_task(db: AsyncSession, task: TaskCreate, user_id: int):
    db_task = Task(**task.model_dump(), owner_id=user_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_user_tasks(db: AsyncSession, user_id: int):
    result = await db.execute(select(Task).where(Task.owner_id==user_id))
    return result.scalars().all()