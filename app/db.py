"""
initialization of database connection
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# get database connection string
db_conn_str = os.getenv("DB_URI")
if os.getenv("PROJECT_ENV") == "test":
    db_conn_str = os.getenv("DB_TEST_URI")

# create database engine
engine = create_engine(db_conn_str)

# create connection
db_conn = engine.connect()
