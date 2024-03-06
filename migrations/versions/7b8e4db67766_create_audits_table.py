"""Create audits table

Revision ID: 7b8e4db67766
Revises: f80bc767bf74
Create Date: 2024-03-06 09:46:24.106480

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b8e4db67766'
down_revision: Union[str, None] = 'f80bc767bf74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'audits',
        sa.Column('id', sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.Column('location_id', sa.Integer, sa.ForeignKey("locations.id"), index=True, nullable=False),
        sa.Column('code', sa.String(), nullable=True),
        sa.Column('score', sa.Float(), nullable=True),
        sa.Column('approved_audit', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime, default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('audits')
