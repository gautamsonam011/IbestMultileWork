from fastapi.responses import HTMLResponse
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory= 'templates')
# @app.get('/hello/',response_class= HTMLResponse)
# async def hello(request: Request):
#     return templates.TemplateResponse("hello.html", {"request":request})
    
@app.get('/file.upload',response_class= HTMLResponse)
async def hello(request: Request,name:str):
    return templates.TemplateResponse("hello.html", {"request":request,"name":name})