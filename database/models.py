# Pydantic will help us validate all our data that is going to be saved in a database : 
from pydantic import BaseModel
from datetime import datetime

# Let's define our " Todo " class that will inherit the " BaseModel "  :

class Todo(BaseModel) :
    title : str
    description : str
    is_completed : bool = False
    is_deleted : bool = False
    updated_at : int = int(datetime.timestamp(datetime.now()))
    creation : int = int(datetime.timestamp(datetime.now()))