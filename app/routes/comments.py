from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(
    tags=["comments"]
)


@router.post("/{post_id}")
def create_comment(post_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    new_comment = models.Comment(
        content=comment.content,
        post_id=post_id,
        user_id=comment.user_id   # এখানে user_id যাবে
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@router.get("/{post_id}")
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()
