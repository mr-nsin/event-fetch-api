from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    base_event_id = Column(Integer)
    title = Column(String)
    event_start_date = Column(DateTime)
    event_end_date = Column(DateTime)
    sell_from = Column(DateTime)
    sell_to = Column(DateTime)
    sold_out = Column(Boolean)
    sell_mode = Column(String)

    zones = relationship("Zone", back_populates="event")

class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.event_id"))
    zone_id = Column(Integer)
    capacity = Column(Integer)
    price = Column(Float)
    name = Column(String)
    numbered = Column(Boolean)

    event = relationship("Event", back_populates="zones")
