from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Category
from app.schemas.category import CategoryCreate

async def create_category(db: AsyncSession, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category

async def get_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()
    