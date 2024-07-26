"""create_workout_logs_table

Revision ID: 0253a1ed4b1c
Revises: a113c052cd38
Create Date: 2024-07-13 16:02:18.759612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0253a1ed4b1c'
down_revision: Union[str, None] = 'a113c052cd38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'workout_logs',
        sa.Column('id', sa.BigInteger, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('exercise_id', sa.BigInteger, nullable=False),
        sa.Column('muscle_group_id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.BigInteger, nullable=True),
        sa.Column('weight', sa.Integer, nullable=False),
        sa.Column('reps', sa.Integer, nullable=False),
        sa.Column('sets', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, nullable=False, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp()),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id']),
        sa.ForeignKeyConstraint(['muscle_group_id'], ['muscle_groups.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
    )


def downgrade() -> None:
    op.drop_table('workout_logs')
