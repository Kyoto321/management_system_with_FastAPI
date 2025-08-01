from typing import List
import fastapi
from db.db_setup import get_db
from fastapi import Depends, HTTPException
from pydantic_schemas.course import Course, CourseCreate
from api.utils.courses import get_course, get_courses, create_course
from sqlalchemy.orm import Session

router = fastapi.APIRouter()

@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db = db)
    return courses


@router.post("/courses")
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)


@router.get("courses/{course_id}")
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course
    

@router.patch("courses/{course_id}")
async def update_course():
    return {"courses": []}


@router.delete("courses/{course_id}")
async def delete_course():
    return {"courses": []}







