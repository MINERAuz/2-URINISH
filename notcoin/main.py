from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    balance = 1000  # Bu yerda foydalanuvchi balansini o'zgartirishingiz mumkin
    return templates.TemplateResponse("index.html", {"request": request, "balance": balance})
