from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note_schema import NoteCreate


def create_note(db: Session, note_data: NoteCreate):
    note = Note(**note_data.model_dump())

    db.add(note)
    db.commit()
    db.refresh(note)

    return note


def get_notes(db: Session):
    return db.query(Note).all() # ORM to: SELECT * FROM notes;


def delete_note(db: Session, id: int):
    note = db.query(Note).filter(Note.id == id).first()
    
    if not note:
        return False

    db.delete(note)
    db.commit()

    return True
