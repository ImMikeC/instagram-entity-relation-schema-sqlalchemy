import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

miModelo = declarative_base()

class Photo(miModelo):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    uploaded = Column(Date, nullable=False)
    views = Column(Integer, nullable=False)
    path = Column(String(250), nullable=False)  
    owner_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(Integer, ForeignKey('follower.id'))
    album_id = Column(Integer, ForeignKey('album.id'))


class User(miModelo):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    u_name = Column(String(250), nullable=False)
    u_email = Column(String(250), nullable=False)

class Follower(miModelo):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    f_email = Column(String(250), nullable=False)

class Comment(miModelo):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    content = Column(String(255), nullable=True)
    photo_id = Column(Integer, ForeignKey('photo.id'),nullable=False)
    uploaded_time = Column(Integer, ForeignKey('photo.uploaded'), nullable=False)
    comment_follower_id = Column(Integer, ForeignKey('photo.follower_id'), nullable=False)

class Album(miModelo):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    album_title = Column(String(255), ForeignKey('photo.title'), nullable=True)
    album_description = Column(String(250), ForeignKey('photo.description'), nullable=False)
    album_views = Column(Integer, ForeignKey('photo.views'), nullable=True)

class Tag(miModelo):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    photo_tag_id = Column(String(255), ForeignKey('photo.id'), nullable=True)
    photo_title_id = Column(String(255), ForeignKey('photo.title'), nullable=True)

class Location(miModelo):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    location_short_name = Column(String(255), nullable=True)
    location_name = Column(String(255), ForeignKey('photo.location'), nullable=True)
    location_name = Column(String(255), ForeignKey('photo.location'), nullable=True)
    location_time = Column(Date, ForeignKey('photo.uploaded'), nullable=True)
    




    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
try:
    result = render_er(miModelo, 'Diagrama_4.png')
    print("Success! Check your new diagram file")
except Exception as e:
    print("There was a problem genering your diagram")
    raise e