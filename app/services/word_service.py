from sqlalchemy.orm import Session

from app.models.word import Word
from app.schemas.word_schema import WordCreate


def create_word(db: Session, word_data: WordCreate):
    word = Word(**word_data.model_dump())

    db.add(word)
    db.commit()
    db.refresh(word)

    return word


def get_words(db: Session):
    return db.query(Word).all() # ORM to: SELECT * FROM words;


def delete_word(db: Session, id: int):
    word = db.query(Word).filter(Word.id == id).first()
    
    if not word:
        return False

    db.delete(word)
    db.commit()

    return True
