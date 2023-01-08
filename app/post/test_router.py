"""
test post router
"""
from fastapi import status

from ..db import db_conn
from .model import Post
from ..test_app import test_app


def setup():
    """
    setup (run before all test in this file)
    """
    for i in range(1, 11):
        query = Post.delete().where(Post.c.post_number==f"thisispostnumber{i}")
        db_conn.execute(query)

def teardown():
    """
    setup (run after all test in this file)
    """
    for i in range(1, 11):
        query = Post.delete().where(Post.c.post_number==f"thisispostnumber{i}")
        db_conn.execute(query)

def test_add_post():
    """
    test add post route
    """
    data = {
        "post_number": "thisispostnumber1",
        "title": "This is Post Title",
        "content": "This is Post Content",
        "is_published": True
    }
    resp = test_app.post("/api/posts", json=data)
    assert resp.status_code == status.HTTP_201_CREATED

    res = resp.json()
    assert res["post_number"] == data["post_number"]
    assert res["title"] == data["title"]
    assert res["content"] == data["content"]
    assert res["is_published"] == data["is_published"]

def test_get_post_by_id():
    """
    test get post by id route
    """
    ################## Insert data first ##################
    data = {
        "post_number": "thisispostnumber2",
        "title": "This is Post Title 2",
        "content": "This is Post Content 2",
        "is_published": True
    }
    resp = test_app.post("/api/posts", json=data)
    assert resp.status_code == status.HTTP_201_CREATED
    data["id"] = resp.json()["id"]

    ################## test get post data by id ##################
    resp = test_app.get(f"/api/posts/{data['id']}")
    assert resp.status_code == status.HTTP_200_OK

    res = resp.json()
    assert res["id"] == data["id"]
    assert res["post_number"] == data["post_number"]
    assert res["title"] == data["title"]
    assert res["content"] == data["content"]
    assert res["is_published"] == data["is_published"]

def test_get_posts():
    """
    test get posts route
    """
    ################## Insert data first ##################
    data = {
        "post_number": "thisispostnumber3",
        "title": "This is Post Title 3",
        "content": "This is Post Content 3",
        "is_published": True
    }
    resp = test_app.post("/api/posts", json=data)
    assert resp.status_code == status.HTTP_201_CREATED

    data = {
        "post_number": "thisispostnumber4",
        "title": "This is Post Title 4",
        "content": "This is Post Content 4",
        "is_published": False
    }
    resp = test_app.post("/api/posts", json=data)
    assert resp.status_code == status.HTTP_201_CREATED

    data = {
        "post_number": "thisispostnumber5",
        "title": "This is Post Title 5",
        "content": "This is Post Content 5",
        "is_published": False
    }
    resp = test_app.post("/api/posts", json=data)
    assert resp.status_code == status.HTTP_201_CREATED

    ################## test get post list data ##################
    # test get posts not published
    resp = test_app.get("/api/posts?is_published=0")
    assert resp.status_code == status.HTTP_200_OK

    res = resp.json()
    for item in res:
        assert item["is_published"] == False

    # test get posts published
    resp = test_app.get("/api/posts?is_published=1")
    assert resp.status_code == status.HTTP_200_OK

    res = resp.json()
    for item in res:
        assert item["is_published"] == True

def test_replace_post_by_id():
    """
    test replace post by id route
    """
    ################## Insert data first ##################
    data = {
        "post_number": "thisispostnumber6",
        "title": "This is Post Title 6",
        "content": "This is Post Content 6",
        "is_published": True
    }
    resp = test_app.post("/api/posts", json=data)
    assert resp.status_code == status.HTTP_201_CREATED
    data["id"] = resp.json()["id"]

    ################## test replace post data by id ##################
    new_data = {
        "post_number": "thisispostnumber7",
        "title": "This is Post Title 7",
        "content": "This is Post Content 7",
        "is_published": False
    }
    resp = test_app.put(f"/api/posts/{data['id']}", json=new_data)
    assert resp.status_code == status.HTTP_200_OK

    res = resp.json()
    assert res["id"] == data["id"]
    assert res["post_number"] == new_data["post_number"]
    assert res["title"] == new_data["title"]
    assert res["content"] == new_data["content"]
    assert res["is_published"] == new_data["is_published"]

def test_update_post_by_id():
    """
    test update post by id route
    """
    ################## Insert data first ##################
    data = {
        "post_number": "thisispostnumber8",
        "title": "This is Post Title 8",
        "content": "This is Post Content 8",
        "is_published": True
    }
    resp = test_app.post("/api/posts", json=data)
    assert resp.status_code == status.HTTP_201_CREATED
    data["id"] = resp.json()["id"]

    ################## test update post data by id ##################
    new_data = {
        "post_number": "thisispostnumber9",
    }
    resp = test_app.patch(f"/api/posts/{data['id']}", json=new_data)
    assert resp.status_code == status.HTTP_200_OK

    res = resp.json()
    assert res["id"] == data["id"]
    assert res["post_number"] == new_data["post_number"]
    assert res["title"] == data["title"]
    assert res["content"] == data["content"]
    assert res["is_published"] == data["is_published"]

    new_data2 = {
        "title": "This is Post Title 9",
    }
    resp = test_app.patch(f"/api/posts/{data['id']}", json=new_data2)
    assert resp.status_code == status.HTTP_200_OK

    res = resp.json()
    assert res["id"] == data["id"]
    assert res["post_number"] == new_data["post_number"]
    assert res["title"] == new_data2["title"]
    assert res["content"] == data["content"]
    assert res["is_published"] == data["is_published"]

    new_data3 = {
        "content": "This is Post Content 9",
    }
    resp = test_app.patch(f"/api/posts/{data['id']}", json=new_data3)
    assert resp.status_code == status.HTTP_200_OK

    res = resp.json()
    assert res["id"] == data["id"]
    assert res["post_number"] == new_data["post_number"]
    assert res["title"] == new_data2["title"]
    assert res["content"] == new_data3["content"]
    assert res["is_published"] == data["is_published"]

    new_data4 = {
        "is_published": False,
    }
    resp = test_app.patch(f"/api/posts/{data['id']}", json=new_data4)
    assert resp.status_code == status.HTTP_200_OK

    res = resp.json()
    assert res["id"] == data["id"]
    assert res["post_number"] == new_data["post_number"]
    assert res["title"] == new_data2["title"]
    assert res["content"] == new_data3["content"]
    assert res["is_published"] == new_data4["is_published"]

def test_delete_post_by_id():
    """
    test delete post by id route
    """
    ################## Insert data first ##################
    data = {
        "post_number": "thisispostnumber10",
        "title": "This is Post Title 10",
        "content": "This is Post Content 10",
        "is_published": True
    }
    resp = test_app.post("/api/posts", json=data)
    assert resp.status_code == status.HTTP_201_CREATED
    data["id"] = resp.json()["id"]

    ################## test delete post data by id ##################
    resp = test_app.delete(f"/api/posts/{data['id']}")
    assert resp.status_code == status.HTTP_200_OK
