from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from .mixin import Mixin
from .role import Role



class User(Mixin, SQLModel, table=True):
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password: str = Field(default=None)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    # relationships
    profile: Optional["Profile"] = Relationship(back_populates="user")
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")
    role: Optional[Role] = Relationship(back_populates="users")
 #   customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
 #   customer: Optional["Customer"] = Relationship(back_populates="users")
    
    
    
class Profile(Mixin, SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="profile")
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    phone: str = Field(default=None)
    address: str = Field(default=None)
    city: str = Field(default=None)
    state: str = Field(default=None)
    country: str = Field(default=None)
    zip_code: str = Field(default=None)
    