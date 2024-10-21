from pydantic import BaseModel, Field
from typing import List, Optional

class CourseCreateUpdate(BaseModel):
    title: str = Field(..., max_length=255)
    description: str

    class Config:
        orm_mode = True