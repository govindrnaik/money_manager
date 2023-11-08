from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount('/static', StaticFiles(directory='static'), name='static')

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")


if __name__== "__main__":
    import uvicorn
    uvicorn.run(app="main:app",host="0.0.0.0", port=8000, reload=True)