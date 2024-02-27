"""add_host_nodeid

Revision ID: cb53e2436829
Revises: 6932f008c06d
Create Date: 2024-02-23 20:24:45.373079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb53e2436829'
down_revision = '6932f008c06d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("hosts",
        sa.Column("nodeid", sa.Integer(), nullable=True),
    )
    op.create_foreign_key('fk_hosts_node', 'hosts', 'nodes', ['nodeid'], ['id'])



def downgrade() -> None:
    op.drop_column("hosts", "nodeid")
