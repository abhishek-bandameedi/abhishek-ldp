from typing import List, Union
from fastapi import FastAPI,Query
from pydantic import BaseModel

q_parameter = FastAPI()

# query parameters with type and default values
@q_parameter.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# optional query parameters
@q_parameter.get("/items/")
def read_item(skip: int = 0, limit: int = None):
    return {"skip": skip, "limit": limit}

# query parameters with lists

@q_parameter.get("/items/")
def read_items(q: List[str] = None):
    return {"items": q}

# query parameters that accepts multiple types
@q_parameter.get("/items/")
def read_item(item_id:Union[int,str]):
    return {"items":item_id}

# query parameters with pydantic models
class QueryParams(BaseModel):
    skip: int = 0
    limit: int = 10

@q_parameter.get("/items/")
def read_item(params: QueryParams):
    return {"skip": params.skip, "limit": params.limit}

# query parameters with validation
@q_parameter.get("/items/")
def read_item(skip: int = Query(..., title="Skip items", ge=0), limit: int = Query(10, le=100)):
    return {"skip": skip, "limit": limit}