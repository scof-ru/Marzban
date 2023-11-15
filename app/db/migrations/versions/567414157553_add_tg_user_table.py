"""Add tg user table

Revision ID: 567414157553
Revises: fc01b1520e72
Create Date: 2023-10-14 13:43:40.565499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '567414157553'
down_revision = 'fc01b1520e72'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tg_users',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('username', sa.String(256), nullable=True),
                    sa.Column('firstname', sa.String(256), nullable=True),
                    sa.Column('lastname', sa.String(256), nullable=True),
                    sa.Column('lang', sa.String(8), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=False),
                    sa.Column('referent', sa.BigInteger(), nullable=True),
                    sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE')),
                    sa.PrimaryKeyConstraint('id'),
                    )
    op.execute('SET NAMES utf8mb4')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tg_users')
    # ### end Alembic commands ###


