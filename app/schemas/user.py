from pydantic import BaseModel, EmailStr, ConfigDict, Field

#Base schema for users
class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    
#Schema for create a user
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=30)
    
#Schema for response without password
class UserResponse(UserBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)