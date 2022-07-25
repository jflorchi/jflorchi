from fastapi import APIRouter
from starlette.responses import FileResponse


router = APIRouter()


@router.get("/", tags=["home", "index"])
async def read_articles():
   return FileResponse("app/files/index.html")

@router.get("/about", tags=["about"])
async def read_about():
    return FileResponse("app/files/about.html")

@router.get("/projects", tags=["projects"])
async def read_about():
    return FileResponse("app/files/projects.html")
