from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ThemeCreateUpdate(BaseModel):
    course_id: int
    title: str = Field(..., max_length=255)
    description: str
    content: str


class ThemeResponse(BaseModel):
    id: int
    course_id: int
    title: str
    description: str
    content: str
    updated_at: datetime
