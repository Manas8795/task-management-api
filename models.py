from sqlalchemy import Column , String , Integer
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key = True,index = True)
    name = Column(String,nullable = False)
    duration = Column(Integer,nullable = False)