from fastapi import APIRouter, Depends
from app import models, schemas
from typing import List
from app.database import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/projects", response_model=List[schemas.Project], tags=["projects"])
async def read_projects_meta(db: Session = Depends(get_db)):
    projects = db.query(models.Projects).all()
    return projects


@router.get("/projects/meta", tags=["projects"])
async def read_projects_meta(db: Session = Depends(get_db)):
    projects = db.query(models.Projects).order_by(models.Projects.start_date.desc()).all()
    resp = []
    for prj in projects:
        tmp = {
            "id": prj.id,
            "title": prj.title,
            "summary": prj.summary,
            "created_at": prj.created_at
        }
        resp.append(tmp)
    return resp

@router.get("/projects/recent", tags=["projects", "recent"])
async def read_projects_meta(db: Session = Depends(get_db)):
    projects = db.query(models.Projects).order_by(models.Projects.start_date.desc()).all()
    resp = []
    count = 0
    for prj in projects:
        tmp = {
            "id": prj.id,
            "title": prj.title,
            "summary": prj.summary,
            "created_at": prj.created_at
        }
        resp.append(tmp)
        count += 1
        if count == 3:
            break
    return resp

@router.get("/projects/{id}", response_model=schemas.Project, tags=["projects"])
async def read_project(id: int, db: Session = Depends(get_db)):
    projects = db.query(models.Projects).filter(models.Projects.id == id).all()
    if len(projects) == 0:
        return {"detail": "Project not found"}
    return projects[0]