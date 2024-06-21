"""create muscle_groups table

Revision ID: 6eac72362dc9
Revises: 9284736f660a
Create Date: 2024-06-21 12:23:17.948499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6eac72362dc9'
down_revision: Union[str, None] = '9284736f660a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'muscle_groups',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), unique=True, index=True, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('muscle_groups')

