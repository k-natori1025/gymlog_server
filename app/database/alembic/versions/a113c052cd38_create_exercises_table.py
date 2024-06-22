"""create exercises table

Revision ID: a113c052cd38
Revises: 6eac72362dc9
Create Date: 2024-06-21 15:57:42.524574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a113c052cd38'
down_revision: Union[str, None] = '6eac72362dc9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'exercises',
        sa.Column('id', sa.BigInteger, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('muscle_group_id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.BigInteger, nullable=False),
        sa.Column('is_custom', sa.Boolean, nullable=False, default=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, nullable=False, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp()),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['muscle_group_id'], ['muscle_groups.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
    )


def downgrade() -> None:
    op.drop_table('exercises')
