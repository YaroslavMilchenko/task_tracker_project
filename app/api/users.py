from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import user_services
from app.api.deps import get_current_user
from app.services.email_service import send_welcome_email

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user_endpoint(
    user:UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
    ):
    try:
        new_user = await user_services.create_user(db=db, user=user)
        background_tasks.add_task(send_welcome_email, new_user.email)
        return new_user
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="User with this email already exists")
        
    

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user