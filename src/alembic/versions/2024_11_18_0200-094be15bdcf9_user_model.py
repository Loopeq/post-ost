"""User model

Revision ID: 094be15bdcf9
Revises: 
Create Date: 2024-11-18 02:00:00.962715

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "094be15bdcf9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("disabled", sa.Boolean(), nullable=False),
        sa.Column("superuser", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.UUID, existing_type=sa.UUID(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_users_uuid"), "users", ["uuid"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
