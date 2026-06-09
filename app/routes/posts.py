from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/")
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(
        content=post.content,
        user_id=post.user_id,
        forum_id=post.forum_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()
