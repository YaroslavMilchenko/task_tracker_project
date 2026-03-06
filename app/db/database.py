from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.core.config import settings
import os

ACTUAL_DATABASE_URL = os.getenv("DATABASE_URL", settings.DATABASE_URL)

engine = create_async_engine(ACTUAL_DATABASE_URL, echo=True)

# Create a factory for async sessions
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for all our database models
Base = declarative_base()

# Dependency function to get a database session in our endpoints
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session