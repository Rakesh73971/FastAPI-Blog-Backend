"""adding content column to posts table

Revision ID: 654f301aefcb
Revises: 750d14d809ef
Create Date: 2025-12-16 11:57:07.465687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '654f301aefcb'
down_revision: Union[str, Sequence[str], None] = '750d14d809ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
