from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class ZoneBase(BaseModel):
    zone_id: int
    capacity: int
    price: float
    name: str
    numbered: bool

class EventBase(BaseModel):
    event_id: int
    base_event_id: int
    title: str
    event_start_date: datetime
    event_end_date: datetime
    sell_from: datetime
    sell_to: datetime
    sold_out: bool
    sell_mode: str
    zones: List[ZoneBase]

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    pass
