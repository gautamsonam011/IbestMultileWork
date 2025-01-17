from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/home/', response_class=HTMLResponse)

def home(request:Request):
    context = {'request':request}
    return templates.TemplateResponse("index.html", context)