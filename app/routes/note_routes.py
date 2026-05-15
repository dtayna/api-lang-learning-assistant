from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.note_schema import NoteCreate, NoteResponse
from app.services import note_service

router = APIRouter()


@router.post("/", response_model=NoteResponse)
def create_note(note_data: NoteCreate, db: Session = Depends(get_db)):
    return note_service.create_note(db, note_data)


@router.get("/", response_model=list[NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    return note_service.get_notes(db)


@router.delete("/{id}", response_model=bool)
def delete_note(id: int, db: Session = Depends(get_db)):
    return note_service.delete_note(db, id)