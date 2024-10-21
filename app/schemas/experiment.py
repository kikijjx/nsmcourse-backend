from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

class ExperimentCreateUpdate(BaseModel):
    theme_id: int
    title: str = Field(..., max_length=255)
    description: str
    parameters: dict

    class Config:
        orm_mode = True