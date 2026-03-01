from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

#Base field
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    
#Schema for create new task
class TaskCreate(TaskBase):
    pass

#Schema for response 
class TaskResponse(TaskBase):
    id: int
    is_complete: bool
    created_at: datetime
    owner_id: int
    
    model_config = ConfigDict(from_attributes=True)