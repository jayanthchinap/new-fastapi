from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    firstName: str
    lastName: str
    DOB: str
    skill: str
    available: str
    


class UserCreate(UserBase):
    firstName: str
    lastName: str
    DOB: str
    skill: str
    available: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True