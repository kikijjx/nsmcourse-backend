from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.theme import Theme
from app.models.course import Course
from app.models.user import User
from app.models.experiment import Experiment
from app.schemas.course import CourseCreateUpdate, CourseResponse


course_router = APIRouter()

@course_router.get("/courses", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    if not courses:
        raise HTTPException(status_code=404, detail="courses not found")
    return courses

@course_router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreateUpdate, db: Session = Depends(get_db)):
    db_course = Course(
        title=course.title,
        description=course.description
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@course_router.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseCreateUpdate, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    db_course.title = course.title
    db_course.description = course.description
    db.commit()
    db.refresh(db_course)
    return db_course

@course_router.delete("/courses/{course_id}", response_model=dict)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    db.delete(db_course)
    db.commit()
    return {"detail": "Course deleted successfully"}
