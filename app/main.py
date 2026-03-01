from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from app.api.routes import router
from app.config import settings

app = FastAPI(title=settings.app_name)

# High performance compression
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Static files with 1 year cache for SEO speed
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)
