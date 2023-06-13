from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

# uvicorn main:app --reload --host=0.0.0.0 --port=8000

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)  # URL
async def home(request: Request):  # VIEW
    names = ["Инна", "Ольа", "Юля"]  # MODEL
    return templates.TemplateResponse("index.html", {"request": request, "names": names})  # TEMPLATE
