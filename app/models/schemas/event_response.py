from pydantic import BaseModel
from datetime import datetime

class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    starts_at: datetime
    ends_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True