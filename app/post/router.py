"""
post router
"""
from datetime import datetime
import logging
import traceback

from fastapi import APIRouter, Response, status
from fastapi.encoders import jsonable_encoder

from ..db import db_conn
from .model import Post
from .schema import PostSchemaInsert, PostSchemaUpdate


router = APIRouter()

@router.post("")
def add_post(post: PostSchemaInsert, resp: Response):
    """
    add post route
    """
    # begin transaction
    tx = db_conn.begin()
    try:
        # get data from body JSON
        decoded_post = jsonable_encoder(post)
        decoded_post["published_at"] = None
        if decoded_post["is_published"]:
            decoded_post["published_at"] = datetime.now()

        decoded_post["created_at"] = datetime.now()
        decoded_post["updated_at"] = datetime.now()

        # insert data to database (return id)
        query = Post.insert().values(**decoded_post)
        res = dict(db_conn.execute(query).returned_defaults)
        res.update(decoded_post)

        # commit transaction
        tx.commit()

        # return response
        resp.status_code = status.HTTP_201_CREATED
        return res

    except Exception as err:
        logging.error(traceback.format_exc())

        # rollback transaction
        tx.rollback()

        # return error response is exception occured
        res = {"message": str(err)}
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return res

@router.get("/{id}")
def get_post_by_id(id: int, resp: Response):
    """
    get post by id route
    """
    try:
        query = Post.select().where(Post.c.id==id)
        data = db_conn.execute(query).first()
        resp.status_code = status.HTTP_200_OK
        return data

    except Exception as err:
        logging.error(traceback.format_exc())

        # return error response is exception occured
        res = {"message": str(err)}
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return res

@router.get("")
def get_posts(resp: Response, is_published: int | None = None):
    """
    get posts route
    """
    try:
        query = Post.select()
        if is_published != None:
            query = query.where(Post.c.is_published==bool(is_published))

        data = db_conn.execute(query).fetchall()
        resp.status_code = status.HTTP_200_OK
        return data

    except Exception as err:
        logging.error(traceback.format_exc())

        # return error response is exception occured
        res = {"message": str(err)}
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return res

@router.put("/{id}")
def replace_post_by_id(id: int, post: PostSchemaInsert, resp: Response):
    """
    replace post by id route
    """
    # begin transaction
    tx = db_conn.begin()
    try:
        # get data from body JSON
        decoded_post = jsonable_encoder(post)
        decoded_post["published_at"] = None
        if decoded_post["is_published"]:
            decoded_post["published_at"] = datetime.now()
        decoded_post["updated_at"] = datetime.now()

        # replace data in database
        query = Post.update().where(Post.c.id==id).values(**decoded_post)
        db_conn.execute(query)

        # get data for return value
        query = Post.select().where(Post.c.id==id)
        res = db_conn.execute(query).first()

        # commit transaction
        tx.commit()

        # return response
        resp.status_code = status.HTTP_200_OK
        return res

    except Exception as err:
        logging.error(traceback.format_exc())

        # rollback transaction
        tx.rollback()

        # return error response is exception occured
        res = {"message": str(err)}
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return res

@router.patch("/{id}")
def update_post_by_id(id: int, post: PostSchemaUpdate, resp: Response):
    """
    update post by id route
    """
    # begin transaction
    tx = db_conn.begin()
    try:
        # get data from body JSON
        decoded_post = jsonable_encoder(post)
        decoded_post["published_at"] = None
        if decoded_post["is_published"]:
            decoded_post["published_at"] = datetime.now()
        decoded_post["updated_at"] = datetime.now()

        # update at least one field data in database
        values = {}
        if decoded_post["post_number"] != None:
            values.update({"post_number": decoded_post["post_number"]})
        if decoded_post["title"] != None:
            values.update({"title": decoded_post["title"]})
        if decoded_post["content"] != None:
            values.update({"content": decoded_post["content"]})
        if decoded_post["is_published"] != None:
            values.update({"is_published": decoded_post["is_published"]})

        query = Post.update().where(Post.c.id==id).values(**values)
        db_conn.execute(query)

        # get data for return value
        query = Post.select().where(Post.c.id==id)
        res = db_conn.execute(query).first()

        # commit transaction
        tx.commit()

        # return response
        resp.status_code = status.HTTP_200_OK
        return res

    except Exception as err:
        logging.error(traceback.format_exc())

        # rollback transaction
        tx.rollback()

        # return error response is exception occured
        res = {"message": str(err)}
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return res

@router.delete("/{id}")
def delete_post_by_id(id: int, resp: Response):
    """
    delete post by id route
    """
    # begin transaction
    tx = db_conn.begin()
    try:
        # delete post in database
        query = Post.delete().where(Post.c.id==id)
        db_conn.execute(query)

        # get data for checking post already deleted
        query = Post.select().where(Post.c.id==id)
        res = db_conn.execute(query).first()
        if res != None:
            raise Exception("Delete post failed!")

        # commit transaction
        tx.commit()

        # return response
        resp.status_code = status.HTTP_200_OK
        return {"message": "Delete post success!"}

    except Exception as err:
        logging.error(traceback.format_exc())

        # rollback transaction
        tx.rollback()

        # return error response is exception occured
        res = {"message": str(err)}
        resp.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return res
