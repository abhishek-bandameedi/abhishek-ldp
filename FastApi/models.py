from pydantic import BaseModel,Field
from fastapi import FastAPI
from typing import List
from pydantic import validator

model = FastAPI()

stored_items = []

# Pydantic model
class Item(BaseModel):
    name:str
    description:str=None
    price:float

# post method to store data
@model.post("/items/")
def create_item(item:Item):
    stored_items.append(item.dict())
    return item

@model.get("/items/", response_model=List[Item])
def read_item():
    return stored_items


# custom field validation

class ItemWithValidation(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name of the item")
    price: float = Field(..., gt=0, description="Price of the item")

valid_items=[]
@model.post("/validitems/")
def create_item_with_validation(item: ItemWithValidation):
    valid_items.append(item.dict())
    return item

@model.get("/validitems/")
def get_valid_items():
    return valid_items


# nested models

class Image(BaseModel):
    url:str
    name:str

class ItemWithImage(BaseModel):
    name:str
    description:str=None
    price:float
    image:Image


# custom validation functions

class ItemWithCustomValidation(BaseModel):
    name:str
    price:float

    @validator("price")
    def validate_price(self,val):
        if val<0:
            raise ValueError("Price cannot be negative")
        return val
    

# converting pydantic model instance to dictionary
# item_dict=item.dict()

# converting pydantic model instance to JSON string
# item_json=item.json()

# schema refers to a structured representation of data, typically defined using Pydantic models.
# Schemas in FastAPI serve multiple purposes, including automatic data validation, serialization, and generation of interactive API documentation.
