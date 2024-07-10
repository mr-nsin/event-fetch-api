from fastapi import APIRouter, HTTPException, Query
from app.db.repositories import EventsRepository
from app.dependencies.fetch import fetch_events
from app.schemas.event import EventCreate, EventResponse
from typing import List
from datetime import datetime

router = APIRouter()
events_repo = EventsRepository()

@router.get("/events", response_model=List[EventResponse])
async def get_events(starts_at: datetime, ends_at: datetime):
    # Fetch events from external provider
    events = fetch_events()
    
    # If events were successfully fetched, store/update them in the database
    if events:
        events_repo.create_or_update_events(events)
    
    # Retrieve events from the database
    filtered_events = events_repo.get_events_by_date_range(starts_at, ends_at)

    return filtered_events
