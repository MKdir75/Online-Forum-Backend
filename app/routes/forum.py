from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(
    tags=["forum"]
)

@router.get("/")
def get_forums(db: Session = Depends(get_db)):
    return db.query(models.Forum).all()

@router.get("/{id}")
def get_forum(id: int, db: Session = Depends(get_db)):
    forum = db.query(models.Forum).filter(models.Forum.id == id).first()
    if not forum:
        return {"error": "Forum not found"}
    return forum

@router.post("/")
def create_forum(forum: schemas.ForumCreate, db: Session = Depends(get_db)):
    new_forum = models.Forum(
        title=forum.title,
        description=forum.description,
        author=forum.author,
        upvotes=forum.upvotes
    )
    db.add(new_forum)
    db.commit()
    db.refresh(new_forum)
    return new_forum
