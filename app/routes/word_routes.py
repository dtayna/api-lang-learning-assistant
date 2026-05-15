from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.word import Word
from app.schemas.word_schema import WordCreate, WordResponse

router = APIRouter()


@router.post("/", response_model=WordResponse)
def create_word(word_data: WordCreate, db: Session = Depends(get_db)):
    word = Word(**word_data.model_dump())

    db.add(word)
    db.commit()
    db.refresh(word)

    return word


@router.get("/", response_model=list[WordResponse])
def get_words(db: Session = Depends(get_db)):
    return db.query(Word).all()