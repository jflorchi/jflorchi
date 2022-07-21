from fastapi import APIRouter
from starlette.responses import FileResponse


router = APIRouter()

@router.get("/about", tags=["articles"])
async def read_about():
    return FileResponse("app/tmp/about.json")
