import requests
from app.api.errors.exceptions import CustomHTTPException
from db.models import Event
from xml.etree import ElementTree as ET
from datetime import datetime

def fetch_events_from_provider():
    try:
        response = requests.get("https://provider.code-challenge.feverup.com/api/events")
        response.raise_for_status()
    except requests.RequestException as e:
        raise CustomHTTPException(status_code=503, message="Provider API is not available") from e
    
    events = []
    root = ET.fromstring(response.content)
    for base_event in root.findall('.//base_event'):
        for event in base_event.findall('event'):
            zones = [
                {
                    "zone_id": int(zone.get('zone_id')),
                    "capacity": int(zone.get('capacity')),
                    "price": zone.get('price'),
                    "name": zone.get('name'),
                    "numbered": zone.get('numbered') == 'true'
                }
                for zone in event.findall('zone')
            ]
            events.append(Event(
                event_id=int(event.get('event_id')),
                base_event_id=int(base_event.get('base_event_id')),
                title=base_event.get('title'),
                event_start_date=datetime.fromisoformat(event.get('event_start_date')),
                event_end_date=datetime.fromisoformat(event.get('event_end_date')),
                sell_mode=base_event.get('sell_mode'),
                zones=zones,
                sell_from=datetime.fromisoformat(event.get('sell_from')),
                sell_to=datetime.fromisoformat(event.get('sell_to')),
                sold_out=event.get('sold_out') == 'true'
            ))
    return events
