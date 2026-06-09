from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")


class Forum(Base):
    __tablename__ = "forums"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    author = Column(String, nullable=False)   
    upvotes = Column(Integer, default=0)  

    posts = relationship("Post", back_populates="forum")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    forum_id = Column(Integer, ForeignKey("forums.id"))

    author = relationship("User", back_populates="posts")
    forum = relationship("Forum", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")
