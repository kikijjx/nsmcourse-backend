from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.theme import Theme
from app.models.course import Course
from app.models.user import User
from app.models.experiment import Experiment
from app.schemas.theme import ThemeCreateUpdate, ThemeResponse
from datetime import datetime
from app.core.auth import get_current_user, is_admin

theme_router = APIRouter()

@theme_router.get("/themes")
def get_themes(db: Session = Depends(get_db)):
    themes = db.query(Theme).all()
    if not themes:
        raise HTTPException(status_code=404, detail="themes not found")
    return themes


@theme_router.post("/themes", response_model=ThemeResponse)
def create_theme(
    theme: ThemeCreateUpdate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    is_admin(current_user)
    db_theme = Theme(
        course_id=theme.course_id,
        title=theme.title,
        description=theme.description,
        content=theme.content,
        updated_at=datetime.utcnow(),
        creator_id=current_user.id
    )
    db.add(db_theme)
    db.commit()
    db.refresh(db_theme)
    return db_theme


@theme_router.put("/themes/{theme_id}", response_model=ThemeResponse)
def update_theme(
    theme_id: int, 
    theme: ThemeCreateUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    is_admin(current_user)
    db_theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not db_theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    db_theme.course_id = theme.course_id
    db_theme.title = theme.title
    db_theme.description = theme.description
    db_theme.content = theme.content
    db_theme.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_theme)
    return db_theme


@theme_router.delete("/themes/{theme_id}", response_model=dict)
def delete_theme(
    theme_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    is_admin(current_user)
    db_theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not db_theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    db.delete(db_theme)
    db.commit()
    return {"detail": "Theme deleted successfully"}


@theme_router.get("/themes/{theme_id}", response_model=ThemeResponse)
def get_theme(theme_id: int, db: Session = Depends(get_db)):
    db_theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not db_theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return db_theme
