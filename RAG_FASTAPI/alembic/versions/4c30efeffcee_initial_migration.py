"""initial migration

Revision ID: 4c30efeffcee
Revises: 
Create Date: 2025-11-23 01:20:59.652341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '4c30efeffcee'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass