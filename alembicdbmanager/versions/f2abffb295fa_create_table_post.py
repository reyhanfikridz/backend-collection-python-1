"""create_table_post

Revision ID: f2abffb295fa
Revises:
Create Date: 2023-01-05 13:33:27.113471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2abffb295fa'
down_revision = None
branch_labels = None
depends_on = None


# process when migrate
def upgrade() -> None:
    # create table post
    op.create_table(
        "post",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('post_number', sa.String(20), nullable=False, unique=True),
        sa.Column('title', sa.String(100), nullable=False),
        sa.Column('content', sa.Text, nullable=False),
        sa.Column('is_published', sa.Boolean, nullable=False),
        sa.Column('published_at', sa.DateTime, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )


# process when rollback migrate
def downgrade() -> None:
    op.drop_table('post')
