from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String)
    content = Column(String)
    creator = Column(String)
    time_stamp = Column(DateTime)
