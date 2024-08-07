"""create users table

Revision ID: 9284736f660a
Revises: 
Create Date: 2024-06-06 15:56:04.764168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9284736f660a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('firebase_uid', sa.String(255), unique=True, nullable=False, index=True),
        sa.Column('name', sa.String(255), unique=True, nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=True),
        sa.Column('password', sa.String(255), nullable=True),
        sa.Column('google_id', sa.String(100), unique=True, nullable=True),
        sa.Column('twitter_id', sa.String(100), unique=True, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, nullable=False, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp()),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
        sa.UniqueConstraint('email'),
    )


def downgrade() -> None:
    op.drop_table('users')
