from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

class ExperimentCreateUpdate(BaseModel):
    theme_id: int
    title: str = Field(..., max_length=255)
    description: str
    parameters: Optional[dict]

class ExperimentResponse(BaseModel):
    id: int
    theme_id: int
    title: str
    description: str
    parameters: Optional[dict]
    updated_at: datetime