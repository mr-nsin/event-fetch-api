from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from db.repositories.base import Base

class Event(Base):
    __tablename__ = "events"
    
    base_event_id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer)    
    title = Column(String)
    event_start_date = Column(DateTime)
    event_end_date = Column(DateTime)
    sell_from = Column(DateTime)
    sell_to = Column(DateTime)
    sold_out = Column(Boolean)
    sell_mode = Column(String)

    zones = relationship("Zone")