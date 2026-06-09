from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class ForumCreate(BaseModel):
    title: str
    description: str
    author: str
    upvotes: int = 0

class ForumOut(BaseModel):
    id: int
    title: str
    description: str
    author: str
    upvotes: int
    class Config:
        orm_mode = True
class PostCreate(BaseModel):
    content: str
    user_id: int
    forum_id: int
    
class PostOut(BaseModel):
    id: int
    content: str
    author: UserOut
    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    content: str
    user_id: int


class CommentOut(BaseModel):
    id: int
    content: str
    author: UserOut
    class Config:
        orm_mode = True
