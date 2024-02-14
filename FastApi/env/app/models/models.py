from typing import Optional
from sqlalchemy import Column, Integer, String
from app.db.base import Base
from pydantic import BaseModel,ConfigDict

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class Post(PostBase):
    __tablename__ = 'posts'

    id:int = Column(Integer, primary_key=True, index=True)

class UserBase(BaseModel):
    username:str

class UserUpdate(BaseModel):
    username:Optional[str]=None
    class Config:
        orm_mode=True