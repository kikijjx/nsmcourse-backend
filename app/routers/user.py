from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import User
user_router = APIRouter()

