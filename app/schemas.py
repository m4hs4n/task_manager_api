from pydantic import BaseModel




class TaskCreate(BaseModel):
    title : str
    description : str = None #it's an optional field
    duration_min : int = None

class TaskResponse(BaseModel):
    id : str
    title : str
    done : bool = False
    description : str = None 
    duration_min : int = None

class TaskUpdate(BaseModel):
    title : str = None
    description : str = None
    duration_min : int = None
    done : bool = None
