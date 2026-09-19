from typing import Optional
from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    name : str
    duration : int

class TaskUpdate(BaseModel):
    name : Optional[str] = None
    duration : Optional[int] = None

UpdateTask = TaskUpdate

class TaskResponse(BaseModel): # this schema will be used to return the database records to the client
    id: int
    name: str
    duration: int

    model_config = ConfigDict(from_attributes=True) # allows pydantic to convert the sqlalchemy Task object into the API response
