from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from routes import service_root, scrapper_service

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(service_root.router, prefix="/api/v1")
app.include_router(scrapper_service.router, prefix="/api/v1/scrapper")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="UF API",
        version="1.0.0",
        description="API to get the UF value",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://homer.sii.cl/responsive/images/logo.jpg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
