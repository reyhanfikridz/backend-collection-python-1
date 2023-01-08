"""
initialization of fastapi application
"""
from fastapi import FastAPI
from .post.router import router as post_router

# init fastapi application
app = FastAPI()

# add post router to app
app.include_router(post_router, prefix="/api/posts", tags=['post'])
