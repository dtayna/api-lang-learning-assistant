from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.word_schema import WordCreate, WordResponse
from app.services import word_service

router = APIRouter()


@router.post("/", response_model=WordResponse)
def create_word(word_data: WordCreate, db: Session = Depends(get_db)):
    return word_service.create_word(db, word_data)


@router.get("/", response_model=list[WordResponse])
def get_words(db: Session = Depends(get_db)):
    return word_service.get_words(db)


@router.delete("/{word_id}", response_model=bool)
def delete_word(word_id: int, db: Session = Depends(get_db)):
    return word_service.delete_word(db, word_id)