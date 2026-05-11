from fastapi import FastAPI, HTTPException
from app.schemas import TaskCreate, TaskResponse, TaskUpdate
import uuid


app = FastAPI()

tasks = ["study", "yoga", "clean", "apply", "watch series"]
#the list of dictionary
tasks_database = [{'id': "00", 'title': "study", 'done':False , 'description': "keep going", 'duration_min': 60},
              {'id': "01", 'title': "yoga", 'done':False , 'description': "you'll have perfect body", 'duration_min': 30},
              {'id': "02", 'title': "clean", 'done':False , 'description': "", 'duration_min': 15},
              {'id': "03", 'title': "apply", 'done':False , 'description': "dream job's waiting", 'duration_min': 60},
              {'id': "04", 'title': "watch series", 'done':False , 'description': "relax", 'duration_min': 30}]




@app.get("/")
def root():
    return {"message": "Task Manager API is running"}

@app.get("/tasks")
def all_tasks():
    return tasks_database
    

@app.post("/tasks")
def Create_task(task: TaskCreate):
    task_response = TaskResponse(id=str(uuid.uuid4()), title=task.title, done=False, description=task.description, duration_min=task.duration_min)
    tasks_database.append(task_response)
    return task_response

@app.delete("/tasks/{to_delete_id}") # the {} means "this part of the URL is a variable"
def delete_task(to_delete_id:str):
    flag : bool = False
    for task in tasks_database:
        if task["id"] == to_delete_id:
            tasks_database.remove(task)
            flag = True
    if flag is True:
        return{"success": True, "message": "Task deleted!"}        
    else:
        raise HTTPException(status_code=404, detail="Task didn't found")
        

@app.put("/task/{to_update_id}")
def update(to_update_id: str, to_update: TaskUpdate):   
    flag : bool = False
    for i,task in enumerate(tasks_database):
        if task["id"] == to_update_id:
            if to_update.title is not None:
                task["title"] = to_update.title
            if to_update.description is not None:
                task["description"] = to_update.description
            if to_update.duration_min is not None:
                task["duration_min"] = to_update.duration_min
            if to_update.done is not None:
                task["done"] = to_update.done       
            flag = True
    if flag is True:
        return{"success": True, "message": "Task modified!"}
    else:
        raise HTTPException(status_code=404, detail="Task didn't found")