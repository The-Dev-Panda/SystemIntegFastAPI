from pydantic import BaseModel
from typing import Optional

# Users
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str
    role: str

    class Config:
        orm_mode = True  # In Pydantic v2, use from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str]
    phone_number: Optional[str]

class ChangePassword(BaseModel):
    current_password: str
    new_password: str

# Todos 
class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True  # In Pydantic v2, use from_attributes = True
