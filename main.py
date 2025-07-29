from fastapi import FastAPI
from src.routes.reg_linear_router import model_router
from src.routes.llm_resume_router import llm_router
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/templates"), name="static")
templates = Jinja2Templates(directory="src/templates")

@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/grasa_corp", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("grasa_corp.html", {"request": request})

@app.get("/resume", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("resumen.html", {"request": request})

app.include_router(router=model_router)
app.include_router(router=llm_router)