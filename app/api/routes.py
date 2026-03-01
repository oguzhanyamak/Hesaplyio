from fastapi import APIRouter, Request, HTTPException, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from app.calculators.registry import registry
from app.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
templates.env.globals["settings"] = settings

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page listing all calculators."""
    all_calculators = registry.get_all()
    
    # Create serializable version for Alpine.js search
    serializable_calcs = [
        {
            "id": c.get("id"),
            "slug": c.get("slug"),
            "category": c.get("category"),
            "title": c.get("title"),
            "description": c.get("description")
        } for c in all_calculators
    ]
    
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "calculators": serializable_calcs
        }
    )

@router.get("/{calculator_slug}", response_class=HTMLResponse)
async def serve_calculator_page(request: Request, calculator_slug: str):
    """Serves the visually stunning, SSR optimized calculator page."""
    calc_config = registry.get_by_slug(calculator_slug)
    if not calc_config:
        raise HTTPException(status_code=404, detail="Calculator not found")
    
    return templates.TemplateResponse(
        "calculator_page.html", 
        {
            "request": request, 
            "config": calc_config,
        }
    )

@router.get("/robots.txt")
async def robots():
    """Tells search engines what to crawl."""
    content = f"User-agent: *\nAllow: /\nSitemap: {settings.domain}/sitemap.xml"
    return Response(content=content, media_type="text/plain")

@router.get("/sitemap.xml")
async def sitemap():
    """Dynamic sitemap for Google indexing."""
    calculators = registry.get_all()
    now = datetime.now().strftime("%Y-%m-%d")
    
    # Static pages (Home)
    urls = [f"<url><loc>{settings.domain}/</loc><lastmod>{now}</lastmod><priority>1.0</priority></url>"]
    
    # Dynamic calculator pages
    for calc in calculators:
        urls.append(
            f"<url><loc>{settings.domain}/{calc['slug']}</loc><lastmod>{now}</lastmod><priority>0.8</priority></url>"
        )
    
    xml_content = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>"
    return Response(content=xml_content, media_type="application/xml")

@router.post("/api/calculate/{calculator_slug}")
async def perform_calculation(calculator_slug: str, payload: dict):
    """Alpine.js calls this endpoint asynchronously to get results instantly."""
    calc_config = registry.get_by_slug(calculator_slug)
    if not calc_config:
        raise HTTPException(status_code=404)
    
    try:
        # FastAPI might receive strings for form data depending on implementation
        # Here AlpineJS will send perfectly JSON formatted data
        results = calc_config["logic_function"](**payload)
        return {"status": "success", "data": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}
