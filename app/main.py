from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from app.api.routes import router
from app.config import settings
import os

app = FastAPI(title=settings.app_name)

# High performance compression
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Custom StaticFiles to add aggressive cache headers for PageSpeed (1 year)
class CachedStaticFiles(StaticFiles):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
        return response

# Static files with 1 year cache for SEO speed
if os.path.exists("app/static"):
    app.mount("/static", CachedStaticFiles(directory="app/static"), name="static")

app.include_router(router)
