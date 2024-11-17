from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from database.schemas import all_tasks
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime

app = FastAPI()
router = APIRouter()


# Let's define the " GET " request that gets of fetches all the data in the database:
@router.get("/")
async def get_all_todos():
    # Fetch only data that are not deleted :
    data = collection.find({"is_deleted": False})
    return(all_tasks(data))


# Let's define the " POST " request that inserts or writes the data in the database :
@router.post("/")
async def create_task(new_task:Todo):
    try:
        response = collection.insert_one(dict(new_task))
        return { "status_code" : 200, "id" : str(response.inserted_id)}
    except Exception as error :
        return HTTPException(status_code=500, detail=f"Some error occured {error}")
    

# Let's define the " PUT " request that updates the data in the database :
@router.put("/{task_id}")
async def update_task(task_id:str, updated_task:Todo):
    try:
        id = ObjectId(task_id)
        existing_document = collection.find_one({"_id":id, "is_deleted":False})
        if not existing_document :
            return HTTPException(status_code=404, detail=f"Task doesn't exist.")
        updated_task.updated_at = datetime.timestamp(datetime.now())
        response = collection.update_one({"_id":id}, {"$set":dict(updated_task)})
        return { "status_code" : 200, "message" : "Task updated Succesfully."}  
    except Exception as error :
        return HTTPException(status_code=500, detail=f"Some error occured {error}")
    

# Let's define the " DELETE " request that updates the data in the database :
@router.delete("/{task_id}")
async def delete_task(task_id:str):
    try:
        id = ObjectId(task_id)
        existing_document = collection.find_one({"_id":id, "is_deleted":False})
        if not existing_document :
            return HTTPException(status_code=404, detail=f"Task doesn't exist.")
        # The soft delete " not deleting the data permanently " from the database :
        response = collection.update_one({"_id":id}, {"$set":{"is_deleted" : True}})

        # The soft delete " not deleting the data permanently " from the database :
        # response = collection.delete_one({"_id":id}, {"$set":{"is_deleted" : True}})

        return { "status_code" : 200, "message" : "Task deleted Succesfully."}  
    except Exception as error :
        return HTTPException(status_code=500, detail=f"Some error occured {error}")



app.include_router(router)