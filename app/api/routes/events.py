from fastapi import APIRouter, HTTPException, Query
from api.dependencies.events import EventsRepository
from services.fetch import fetch_events_from_provider
from models.schemas.event_response import EventResponse
from typing import List
from datetime import datetime

event = APIRouter()
events_repo = EventsRepository()

@event.get("/events", response_model=List[EventResponse])
async def get_events(starts_at: datetime, ends_at: datetime):
    print(starts_at, ends_at)
    # Fetch events from external provider
    events = fetch_events_from_provider()
    
    # If events were successfully fetched, store/update them in the database
    if events:
        events_repo.create_or_update_events(events)
    
    # Retrieve events from the database
    filtered_events = events_repo.get_events_by_date_range(starts_at, ends_at)

    return filtered_events
