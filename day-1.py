from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("hello/{name}")
async def hello(name:str):
    return {"name":name}

@app.get("/")
def read_root():
    return {"Hello":"World"}

class Item(BaseModel):
    name:str
    price:float
    is_offer:Union[bool,None]=None
    
@app.get("items/{item_id}")
def read_item(item_id: int,q:Union[bool,None]=None):
    return {"item_id": item_id,"q":q}

@app.put("items/{item_id}")
def update_item(item_id: int,item:Item):
    return {"item_name": item.name,"item_id":item_id}

Item("Sonam",234,True)
    
    

    
