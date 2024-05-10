from fastapi import FastAPI, Body,Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()

list_of_user = list()

templates = Jinja2Templates(directory="templates")

class NameValue(BaseModel):
    name:str=None
    country:str
    age:int
    salary:float
    
@app.get('/home/{user_name}')
async def home_write(request:Request, user_name:str):
    return templates.TemplateResponse("home.html", {"request":request})

    # return {
    #     "name":user_name,
    #     "age":24,
    #     "query":query
    # }


@app.get('/')
def root():
    return {"Hello":"World"}