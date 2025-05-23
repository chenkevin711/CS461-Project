from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal, Base, engine
from app.models import Item
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API is working with Supabase!"}

@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
