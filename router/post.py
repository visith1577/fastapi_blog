import random
import string

from fastapi import APIRouter, Depends, UploadFile
from fastapi.params import File
from sqlalchemy.orm import Session

from database import db_post
from database.database import get_db
from router.schemas import PostBase
import shutil

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('/')
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)


@router.get('/all')
async def get(db: Session = Depends(get_db)):
    return await db_post.get_all(db)


@router.delete('/{id}')
def delete(_id: int, db: Session = Depends(get_db)):
    return db_post.delete(db, _id)


@router.post('/upload')
def upload_image(file: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(6))
    new = f'__{rand_str}__.'
    filename = new.join(file.filename.split('.', 1))
    path = f'images/{filename}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": path}
