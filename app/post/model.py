"""
post model
"""
import sqlalchemy as sa

Post = sa.Table(
    "post", sa.MetaData(),
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('post_number', sa.String(20), nullable=False, unique=True),
    sa.Column('title', sa.String(100), nullable=False),
    sa.Column('content', sa.Text, nullable=False),
    sa.Column('is_published', sa.Boolean, nullable=False),
    sa.Column('published_at', sa.DateTime, nullable=True),
    sa.Column('created_at', sa.DateTime, nullable=False),
    sa.Column('updated_at', sa.DateTime, nullable=False),
)
