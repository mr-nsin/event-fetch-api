from pydantic import BaseModel
from typing import Dict, List
class CustomEvent(BaseModel):
    id: int
    title: str
    start_date: str
    start_time: str
    end_date: str
    end_time: str
    min_price: float
    max_price: float

class EventsResponse(BaseModel):
    data: Dict[str, List[CustomEvent]]
    error: str = None