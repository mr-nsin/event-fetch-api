from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from db.repositories.base import Base


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
