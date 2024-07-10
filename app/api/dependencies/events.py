from sqlalchemy.orm import Session
from models.domain.event import Event
from models.domain.zone import Zone
from datetime import datetime
from typing import List
from db.repositories.base import SessionLocal

class EventsRepository:
    def __init__(self, session: Session = SessionLocal()):
        self.session = session
    
    def create_or_update_events(self, events: List[dict]):
        try:
            for event_data in events:
                event = self.session.query(Event).filter(Event.event_id == event_data['event_id']).first()
                if event:
                    # Update existing event
                    self._update_event(event, event_data)
                else:
                    # Create new event
                    self._create_event(event_data)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    
    def _create_event(self, event_data: dict):
        try:
            new_event = Event(**event_data)
            self.session.add(new_event)
            self.session.flush()  # Force immediate flush to get event_id for zones
            self._create_zones(new_event, event_data['zones'])
        except Exception as e:
            self.session.rollback()
            raise e
    
    def _update_event(self, event: Event, event_data: dict):
        try:
            event.base_event_id = event_data['base_event_id']
            event.title = event_data['title']
            event.event_start_date = event_data['event_start_date']
            event.event_end_date = event_data['event_end_date']
            event.sell_from = event_data['sell_from']
            event.sell_to = event_data['sell_to']
            event.sold_out = event_data['sold_out']
            event.sell_mode = event_data['sell_mode']
            # Update zones
            self.session.query(Zone).filter(Zone.event_id == event.event_id).delete()
            self.session.flush()  # Force immediate flush to clear zones
            self._create_zones(event, event_data['zones'])
        except Exception as e:
            self.session.rollback()
            raise e
    
    def _create_zones(self, event: Event, zones_data: List[dict]):
        try:
            for zone_data in zones_data:
                zone = Zone(event_id=event.event_id, **zone_data)
                self.session.add(zone)
            self.session.flush()  # Force immediate flush for zones
        except Exception as e:
            self.session.rollback()
            raise e
    
    def get_events_by_date_range(self, starts_at: datetime, ends_at: datetime):
        try:
            return self.session.query(Event).filter(
                Event.event_start_date >= starts_at,
                Event.event_end_date <= ends_at
            ).all()
        except Exception as e:
            raise e
