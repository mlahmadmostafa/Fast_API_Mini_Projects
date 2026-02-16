"""Added phone numbers to users

Revision ID: 0f8d48b73303
Revises: 
Create Date: 2026-02-16 15:05:31.880852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f8d48b73303'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # alembic adding a new column to the users table
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "phone_number") # table, column
