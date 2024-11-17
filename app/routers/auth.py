from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.auth import authenticate_user, get_current_user
from app.database.database import get_db
from app.models.user import User
from datetime import datetime
from app.core.auth import hash_password

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@auth_router.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    token = authenticate_user(db, form_data.username, form_data.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    return {"access_token": token, "token_type": "bearer"}

@auth_router.get("/me", response_model=dict)
def get_profile(
    current_user: User = Depends(get_current_user)
):
    return {"email": current_user.email, "username": current_user.username}

@auth_router.post("/register_admin")
def register_admin(
    username: str, 
    email: str, 
    password: str, 
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(password)
    new_user = User(
        username=username,
        email=email,
        password_hash=hashed_password,
        role="admin",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"detail": "Admin registered successfully"}
