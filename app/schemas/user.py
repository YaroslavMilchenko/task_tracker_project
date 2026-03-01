from pydantic import BaseModel, EmailStr, ConfigDict

#Base schema for users
class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    
#Schema for create a user
class UserCreate(UserBase):
    password: str
    
#Schema for response without password
class UserResponse(UserBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)