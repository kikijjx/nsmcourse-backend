from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class UserCreateUpdate(BaseModel):
    username: str = Field(..., max_length=255)
    email: str = Field(..., max_length=255)
    password_hash: str