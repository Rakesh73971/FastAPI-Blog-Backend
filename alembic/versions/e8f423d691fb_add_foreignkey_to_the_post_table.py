"""add foreignkey to the post table

Revision ID: e8f423d691fb
Revises: d0c83b31ab6c
Create Date: 2025-12-16 12:28:39.408922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8f423d691fb'
down_revision: Union[str, Sequence[str], None] = 'd0c83b31ab6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table='posts',referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')