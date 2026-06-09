from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter()

@router.get("/{post_id}")
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()
