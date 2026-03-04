from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

#Base field
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    
#Schema for create new task
class TaskCreate(TaskBase):
    pass

#Schema for response 
class TaskResponse(TaskBase):
    id: int
    is_completed: bool
    created_at: datetime
    owner_id: int
    
    model_config = ConfigDict(from_attributes=True)
    
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    category_id: Optional[int] = None