from fastapi import FastAPI
from typing import Optional
from  pydantic import BaseModel
app = FastAPI()
@app.post('/')
def get_full_name(first_name,last_name):
    Full_name = first_name + ' ' +last_name
    return Full_name
print(get_full_name('Sonam','Gautam'))

@app.get('/')
def say_hi(name:Optional[str]=None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

@app.put('/')
class User(BaseModel):
    id:int
    name:str
    friends: list[int] = []
    
external_data = {
    "id":"123",
    "name":"Sonam",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)

class Item(BaseModel):
    name:str
    description:str | None = None
    price:float
    tax:float |None = None

@app.patch('/items/')
async def create_item(item:Item):
    return item