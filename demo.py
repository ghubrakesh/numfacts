from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import api

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post("/number", response_class=HTMLResponse)
async def get_number_fact(request: Request, number: int = Form(...)):
    response = api.get_fact(number)
    return templates.TemplateResponse('result.html', {'request': request, 'number': number, 'response': response})
