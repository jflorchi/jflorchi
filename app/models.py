from sqlalchemy import TIME, Column, Integer, String
from sqlalchemy.types import Date, TIMESTAMP, Boolean
from .database import Base


class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    summary = Column(String)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    start_date = Column(Date)
    end_date = Column(Date)
    published = Column(Integer)
    content = Column(String)
