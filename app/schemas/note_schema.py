from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: Optional[str] = None
    text: str


class NoteCreate(NoteBase):
    pass


class NoteResponse(NoteBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True