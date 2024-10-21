from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ThemeCreateUpdate(BaseModel):
    course_id: int
    title: str = Field(..., max_length=255)
    content: str

    class Config:
        orm_mode = True