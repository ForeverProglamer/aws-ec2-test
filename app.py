from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_model=dict[str, str])
async def read_root():
    return {'data': 'Hello, world'}


@app.get('/hello/{name}', response_class=HTMLResponse)
async def greet_user(name: str, request: Request):
    return templates.TemplateResponse(
        'greet.html', {'request': request, 'name': name}
    )
