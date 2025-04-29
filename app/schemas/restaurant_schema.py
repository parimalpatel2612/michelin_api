from typing import List, Optional
from pydantic import BaseModel, Field
from .team_member_schema import TeamMember, TeamMemberCreate


class RestaurantBase(BaseModel):
    name: str = Field(..., max_length=100)
    opening_hours: Optional[str] = Field(None, example="Mon-Fri: 11:00-22:00")
    cuisine: str = Field(..., max_length=50)
    has_bar: bool = Field(False)
    district: str = Field(..., max_length=50)
    price_range: int = Field(..., ge=1, le=3, description="1: $, 2: $$, 3: $$$")
    michelin_stars: int = Field(0, ge=0, le=3)

class RestaurantCreate(RestaurantBase):
    team_members: List[TeamMemberCreate] = []

class RestaurantUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    opening_hours: Optional[str] = None
    cuisine: Optional[str] = Field(None, max_length=50)
    has_bar: Optional[bool] = None
    district: Optional[str] = Field(None, max_length=50)
    price_range: Optional[int] = Field(None, ge=1, le=3)
    michelin_stars: Optional[int] = Field(None, ge=0, le=3)

class Restaurant(RestaurantBase):
    id: int
    team_members: List[TeamMember] = []

    class Config:
        orm_mode = True