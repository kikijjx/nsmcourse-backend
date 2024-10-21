from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.theme import Theme
from app.models.course import Course
from app.models.user import User
from app.models.experiment import Experiment


theme_router = APIRouter()

@theme_router.get("/themes")
def get_themes(db: Session = Depends(get_db)):
    themes = db.query(Theme).all()
    if not themes:
        raise HTTPException(status_code=404, detail="themes not found")
    return themes