"""Create locations table

Revision ID: f80bc767bf74
Revises: 
Create Date: 2024-03-06 09:46:15.896709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f80bc767bf74'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'locations',
        sa.Column('id', sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.Column('currency', sa.String(), nullable=True),
        sa.Column('language', sa.String(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('time_zone', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime, default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('locations')
