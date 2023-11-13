from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .mixin import Mixin

class Role(Mixin, SQLModel, table=True):
    name: str = Field(index=True, unique=True)
    description: Optional[str] = Field(default=None)
    # relationships
    users: Optional[List['User']] = Relationship(back_populates="role")
    permissions: Optional[List["Permission"]] = Relationship(back_populates="role")  


class Permission(Mixin, SQLModel, table=True):
    name: str = Field(index=True, unique=True)
    description: Optional[str] = Field(default=None)
    # relationships
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")
    role: Optional[Role] = Relationship(back_populates="permissions")