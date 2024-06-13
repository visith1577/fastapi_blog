import datetime

from fastapi import HTTPException, status

from database.models import Post
from router.schemas import PostBase
from sqlalchemy.orm.session import Session


def create(db: Session, request: PostBase):
    new_post = Post(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        time_stamp=datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


async def get_all(db: Session):
    return db.query(Post).all()


def delete(db: Session, _id: int):
    post = db.query(Post).filter(Post.id.is_(_id)).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not available")
    db.delete(post)
    db.commit()
    return 'ok'
