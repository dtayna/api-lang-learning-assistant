from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class WordBase(BaseModel):
    word: str
    translation: Optional[str] = None
    meaning: Optional[str] = None
    examples: Optional[str] = None


class WordCreate(WordBase):
    pass


class WordResponse(WordBase):
    id: int
    image: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True