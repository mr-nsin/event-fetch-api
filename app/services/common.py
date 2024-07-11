from models.schemas.event_response import EventsResponse, CustomEvent
from models.domain.event import Event
from typing import List

def generate_custom_reponse(events: List[Event]) -> EventsResponse:
    
    total_events = []
    for event in events:
            max_price = max(zone.price for zone in event.zones)
            min_price = min(zone.price for zone in event.zones)
            total_events.append(CustomEvent(id = event.base_event_id,
                                            title = event.title,
                                            start_date = event.event_start_date.strftime('%Y-%m-%d'),
                                            start_time = event.event_start_date.strftime('%H:%M:%S'),
                                            end_date = event.event_end_date.strftime('%Y-%m-%d'),
                                            end_time = event.event_end_date.strftime('%H:%M:%S'),
                                            max_price = max_price,
                                            min_price = min_price))
    event_resp = EventsResponse(data = { "events" : total_events}, errors = None)

    return event_resp
