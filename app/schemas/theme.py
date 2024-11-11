from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from typing import Dict, Any

class Section(BaseModel):
    type: str
    content: str

class ThemeCreateUpdate(BaseModel):
    course_id: int
    title: str = Field(..., max_length=255)
    description: str
    content: Any

class ThemeResponse(BaseModel):
    id: int
    course_id: int
    title: str
    description: str
    content: Any
    updated_at: datetime
