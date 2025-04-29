from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from app.utils.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    opening_hours = Column(String(100))
    cuisine = Column(String(50))
    has_bar = Column(Boolean, default=False)
    district = Column(String(50))
    price_range = Column(Integer)  # 1-3 scale
    michelin_stars = Column(Integer)  # 0-3

    team_members = relationship("TeamMember", back_populates="restaurant")