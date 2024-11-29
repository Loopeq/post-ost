"""UUID index strategy

Revision ID: 452b5bc8a1ee
Revises: ab52a4cd0508
Create Date: 2024-11-21 17:30:22.555517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '452b5bc8a1ee'
down_revision: Union[str, None] = 'ab52a4cd0508'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_strategies_uuid', 'strategies', type_='unique')
    op.create_index(op.f('ix_strategies_uuid'), 'strategies', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_strategies_uuid'), table_name='strategies')
    op.create_unique_constraint('uq_strategies_uuid', 'strategies', ['uuid'])
    # ### end Alembic commands ###
