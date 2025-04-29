from typing import Optional
from pydantic import BaseModel

class TeamMemberBase(BaseModel):
    name: str
    title: Optional[str] = None

class TeamMemberCreate(TeamMemberBase):
    pass

class TeamMemberUpdate(TeamMemberBase):
    pass

class TeamMember(TeamMemberBase):
    id: int
    restaurant_id: int

    class Config:
        orm_mode = True