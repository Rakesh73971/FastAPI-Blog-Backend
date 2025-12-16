"""adding last few columns to the post table

Revision ID: 71a65b60697e
Revises: e8f423d691fb
Create Date: 2025-12-16 12:42:18.952304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71a65b60697e'
down_revision: Union[str, Sequence[str], None] = 'e8f423d691fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('published',sa.Boolean(),server_default='TRUE',nullable=False)),
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('NOW()'),nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published'),
    op.drop_column('posts','created_at')

