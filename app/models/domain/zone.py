from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from db.repositories.base import Base


class Zone(Base):
    __tablename__ = "zones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    zone_id = Column(Integer)
    base_event_id = Column(Integer, ForeignKey("events.base_event_id"))
    capacity = Column(Integer)
    price = Column(Float)
    name = Column(String)
    numbered = Column(Boolean)

    event = relationship("Event", back_populates="zones")
