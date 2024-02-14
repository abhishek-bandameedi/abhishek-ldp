from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# path parameters 

@app.get("/names/{item}")
async def read_item(item):
    return {"item_name": item}

# path parameters with types and query parameters

@app.get("/item/{item_id}")
async def read_item(item_id:int,qp:str=None):
    return {item_id: f"This is item {item_id}","query_parameter":qp}

