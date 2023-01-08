"""
post schema
"""
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class PostSchemaInsert(BaseModel):
    """
    post schema without id
    (for insert/replace data)
    """
    post_number: str
    title: str
    content: str
    is_published: bool


class PostSchemaUpdate(BaseModel):
    """
    post schema without id
    (for update data)
    """
    post_number: str | None
    title: str | None
    content: str | None
    is_published: bool | None
