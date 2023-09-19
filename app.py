from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import api

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post("/number", response_class=HTMLResponse)
async def show(request: Request, number: int = Form(...)):
    fact = api.get_fact(number)
    return templates.TemplateResponse('result.html', {'request': request, 'number': number, 'fact': fact})