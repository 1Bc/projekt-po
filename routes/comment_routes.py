from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from entity.comment import Comment, CommentCreate

router = APIRouter()


@router.get("/comments")
def get_comments(db: Session = Depends(get_db)):
    comments = db.query(Comment).all()
    return comments


@router.post("/comment")
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    db_comment = Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
