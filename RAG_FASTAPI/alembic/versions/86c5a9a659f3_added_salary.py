"""added salary

Revision ID: 86c5a9a659f3
Revises: 4c30efeffcee
Create Date: 2025-11-23 01:34:10.042083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy import String


revision: str = '86c5a9a659f3'
down_revision: Union[str, Sequence[str], None] = '4c30efeffcee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', String(), nullable=False),
    sa.Column('headquarters', String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_name'), 'team', ['name'], unique=False)
    op.add_column('hero', sa.Column('team_id', sa.Integer(), nullable=True))
    op.add_column('hero', sa.Column('salary', sa.Float(), nullable=True))
    op.create_index(op.f('ix_hero_name'), 'hero', ['name'], unique=False)
    op.create_foreign_key('fk_hero_team_id', 'hero', 'team', ['team_id'], ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_hero_team_id', 'hero', type_='foreignkey')
    op.drop_index(op.f('ix_hero_name'), table_name='hero')
    op.drop_column('hero', 'salary')
    op.drop_column('hero', 'team_id')
    op.drop_index(op.f('ix_team_name'), table_name='team')
    op.drop_table('team')