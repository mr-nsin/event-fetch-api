from fastapi import APIRouter, HTTPException, Query
from api.dependencies.events import EventsRepository
from services.fetch import fetch_events_from_provider
from models.schemas.event_response import EventList
from typing import List
from datetime import datetime, timedelta
from services.common import generate_custom_reponse

event = APIRouter()
events_repo = EventsRepository()

@event.get("/search", response_model=EventList, summary="Lists the available events on a time range")
async def get_events(
    starts_at: datetime = Query(default=datetime.now() - timedelta(30), description="Return only events that starts after this date"),
    ends_at: datetime = Query(default=datetime.now(), description="Return only events that finishes before this date")
):
    # Fetch events from external provider
    events = fetch_events_from_provider(start_at=starts_at, ends_at=ends_at)
    
    # If events were successfully fetched, store/update them in the database
    if events:
        events_repo.create_or_update_events(events)
    
    # Retrieve events from the database
    filtered_events = events_repo.get_events_by_date_range(starts_at, ends_at)

    return generate_custom_reponse(filtered_events)
