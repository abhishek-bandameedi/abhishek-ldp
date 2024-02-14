from fastapi import FastAPI
from enum import Enum
from fastapi import Depends


p_parameter = FastAPI()

# path parameter with type
@p_parameter.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# path parameter with default value
@p_parameter.get("/items/{item_id}")
def read_item(item_id: int = 42):
    return {"item_id": item_id}

# path parameters with enumerations

class ItemType(str,Enum):
    small="small"
    medium="medium"
    large="large"

@p_parameter.get("/items/{item_type}")
def read_item(item_type: ItemType):
    return {"item_type": item_type}

# path parameters with paths
@p_parameter.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str):
    return {"user_id": user_id, "item_id": item_id}

# path parameters with dependencies

def get_db_connection():
    # some operation to get the db connection
    return "db_connection"

@p_parameter.get("/items/{item_id}")
def read_item(item_id:int,db:str=Depends(get_db_connection)):
    return {"item_id": item_id, "db_connection": db}

