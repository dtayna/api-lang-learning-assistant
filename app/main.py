from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes.word_routes import router as word_router
from app.models.word import Word

from app.routes.note_routes import router as note_router
from app.models.note import Note

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(word_router, prefix="/words", tags=["Words"])
app.include_router(note_router, prefix="/notes", tags=["Notes"])

@app.get("/")
def root():
    return {"message": "Backend is running"}