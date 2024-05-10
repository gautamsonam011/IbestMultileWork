from fastapi import FastAPI
from pydantic import BaseModel


# @app.get("/login/", response_class=HTMLResponse)
# async def login(request: Request):
#    return templates.TemplateResponse("login.html", {"request": request})


app = FastAPI()
data = []
class Book(BaseModel):
   Id:int
   Tittle:str
   Author:str
   Publisher:str
   
   