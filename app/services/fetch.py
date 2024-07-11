import requests
from models.domain.event import Event
from models.domain.zone import Zone
from xml.etree import ElementTree as ET
from datetime import datetime
from typing import List

def fetch_events_from_provider(start_at: datetime, ends_at: datetime, sell_mode: str = 'online') -> List[Event]:
    try:
        response = requests.get("https://provider.code-challenge.feverup.com/api/events")
        response.raise_for_status()
    except requests.RequestException as e:
        pass
    
    events = []
    root = ET.fromstring(response.content)
    for base_event in root.findall('.//base_event'):
        for event in base_event.findall('event'):
            try:
                sell_mode = base_event.get('sell_mode')
                event_start_date = datetime.fromisoformat(event.get('event_start_date'))
                event_end_date = datetime.fromisoformat(event.get('event_end_date'))

                # Check and filter out only those events which are 'online' and lies between given range
                if sell_mode == 'online' and event_start_date >= start_at and event_end_date <= event_end_date:
                    zones = [
                        Zone(
                            zone_id=int(zone.get('zone_id')),
                            base_event_id=int(base_event.get('base_event_id')),
                            capacity=int(zone.get('capacity')),
                            price=zone.get('price'),
                            name=zone.get('name'),
                            numbered=zone.get('numbered') == 'true'
                        )
                        for zone in event.findall('zone')
                    ]
                    
                    events.append(Event(
                        event_id=int(event.get('event_id')),
                        base_event_id=int(base_event.get('base_event_id')),
                        title=base_event.get('title'),
                        event_start_date=event_start_date,
                        event_end_date=event_end_date,
                        sell_mode=sell_mode,
                        zones=zones,
                        sell_from=datetime.fromisoformat(event.get('sell_from')),
                        sell_to=datetime.fromisoformat(event.get('sell_to')),
                        sold_out=event.get('sold_out') == 'true'
                    ))
            except ValueError as ex:
                print(ex)

    return events
