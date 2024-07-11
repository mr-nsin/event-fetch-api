from pydantic import BaseModel
from typing import Dict, List
class EventSummary(BaseModel):
    id: int
    title: str
    start_date: str
    start_time: str
    end_date: str
    end_time: str
    min_price: float
    max_price: float

class EventList(BaseModel):
    events: List[EventSummary]
    error: str = None