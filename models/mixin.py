from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel


class Mixin(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())
    