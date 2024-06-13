from fastapi import FastAPI
from database import models
from database.database import engine
from fastapi.staticfiles import StaticFiles
from router import post

app = FastAPI()
app.include_router(post.router)


models.Base.metadata.create_all(engine)
app.mount('/images', StaticFiles(directory='images'), name='images')
