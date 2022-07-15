from fastapi import APIRouter

router = APIRouter()

@router.get("/articles/", tags=["articles"])
async def read_articles():
    return [{"idk": 1, "idk2": 2}]


@router.get("/articles/{article_id}")
async def read_article(article_id: int):
    return {"missing": "oops"}