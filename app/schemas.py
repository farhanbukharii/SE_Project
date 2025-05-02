from pydantic import BaseModel
from typing import List
from datetime import datetime

# Base schema for recent search
class RecentSearchBase(BaseModel):
    query: str

# Schema for creating a recent search
class RecentSearchCreate(RecentSearchBase):
    pass

# Schema for returning a recent search
class RecentSearch(RecentSearchBase):
    id: int
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }

# Base schema for user
class UserBase(BaseModel):
    username: str

# Schema for creating a user
class UserCreate(UserBase):
    password: str

# Schema for returning a user
class User(UserBase):
    id: int
    recent_searches: List[RecentSearch] = []

    model_config = {
        "from_attributes": True
    }
