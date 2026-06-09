from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, forum, comments, moderation, posts
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api/users")
app.include_router(forum.router, prefix="/api/forum")
app.include_router(comments.router, prefix="/api/comments")
app.include_router(posts.router, prefix="/api/posts")
app.include_router(moderation.router, prefix="/api/moderation")
