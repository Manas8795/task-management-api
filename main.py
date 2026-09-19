from fastapi import FastAPI , Path , Depends
from typing import Optional
from pydantic import BaseModel
from database import engine ,Base , get_db
from schemas import TaskResponse , TaskCreate , TaskUpdate
from models import Task
from sqlalchemy.orm import Session

Base.metadata.create_all(bind = engine)

app = FastAPI()

@app.get("/get-task-all",response_model = list[TaskResponse])
def index(db:Session = Depends(get_db)): # depends is the fastapi dependecncy injection system  ,
# before running this function go execute get_db() first instead of manually creating databases every single time  
    tasks = db.query(Task).all()
    return tasks

@app.get("/get-task/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        return {"Error": "Task does not exist"}

    return task

@app.post("/post-task",response_model = TaskResponse)
def post_task(task : TaskCreate, db:Session = Depends(get_db)):
    new_task = Task(
        name = task.name,
        duration = task.duration
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/put-task/{task_id}", response_model=TaskResponse)
def put_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if existing_task is None:
        return {"Error": "Task does not exist"}

    if task.name is not None:
        existing_task.name = task.name

    if task.duration is not None:
        existing_task.duration = task.duration

    db.commit()
    db.refresh(existing_task)

    return existing_task


@app.delete("/del-task/{task_id}")
def del_task(task_id: int, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if existing_task is None:
        return {"Error": "Task does not exist"}

    db.delete(existing_task)
    db.commit()

    return {"Msg": "Task deleted successfully"}

# tasks = {
#     1 : {
#         "name" : "laundry",
#         "duration" : 2,
#     }
# }

# @app.get("/get-task-all")
# def index():
#     return tasks


# @app.get("/get-task/{task_id}")
# def get_task(task_id : int):
#     return tasks[task_id]

# @app.post("/post-task/{task_id}")
# def post_task(task_id : int,task : Task):
#     if task_id in tasks:
#         return {"Error" : "Task already exists"}
#     tasks[task_id] = task
#     return tasks[task_id]

# @app.put("/put-task/{task_id}")
# def put_task(task_id : int,task : UpdateTask):
#     if task_id not in tasks:
#         return {"Error " : " record does not exists "}
#     if task.name is not None:
#         tasks[task_id]["name"] = task.name

#     if task.duration is not None:
#         tasks[task_id   ]["duration"] = task.duration

#     return tasks[task_id]

# @app.delete("/del-task/{task_id}")
# def del_task(task_id:int):
#     if task_id not in tasks:
#         return {"Error" : "Record does not exists"}
#     del tasks[task_id]
#     return {"Msg" : "student deleted successfully"}