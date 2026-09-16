from fastapi import FastAPI , Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

tasks = {
    1 : {
        "name" : "laundry",
        "duration" : 2,
    }
}
class Task(BaseModel):
    name : str
    duration : int

class UpdateTask(BaseModel):
    name : Optional[str] = None
    duration : Optional[int] = None

@app.get("/get-task-all")
def index():
    return tasks


@app.get("/get-task/{task_id}")
def get_task(task_id : int):
    return tasks[task_id]

@app.post("/post-task/{task_id}")
def post_task(task_id : int,task : Task):
    if task_id in tasks:
        return {"Error" : "Task already exists"}
    tasks[task_id] = task
    return tasks[task_id]

@app.put("/put-task/{task_id}")
def put_task(task_id : int,task : UpdateTask):
    if task_id not in tasks:
        return {"Error " : " record does not exists "}
    if task.name is not None:
        tasks[task_id]["name"] = task.name

    if task.duration is not None:
        tasks[task_id   ]["duration"] = task.duration

    return tasks[task_id]

@app.delete("/del-task/{task_id}")
def del_task(task_id:int):
    if task_id not in tasks:
        return {"Error" : "Record does not exists"}
    del tasks[task_id]
    return {"Msg" : "student deleted successfully"}