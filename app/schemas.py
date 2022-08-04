from datetime import date, datetime
from re import S
from pydantic import BaseModel
from typing import Optional


class Project(BaseModel):
    id: Optional[int]
    title: Optional[str]
    summary: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    start_date: Optional[date]
    end_date: Optional[date]
    published: Optional[int]
    content: Optional[str]
    
    class Config:
        orm_mode = True
