from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .mixin import Mixin
from .user import User

class Customer(Mixin, SQLModel, table=True):
    name: str = Field(index=True, unique=True)
    description: Optional[str] = Field(default=None)
    address: str = Field(default=None)
    phone: str = Field(default=None)
    # relationships
    users: Optional[List["User"]] = Relationship(back_populates="customer")
    