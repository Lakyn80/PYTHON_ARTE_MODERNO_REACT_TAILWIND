"""Add timezone to Order

Revision ID: cdaffa79f42e
Revises: dfe758c4bda5
Create Date: 2025-03-16 02:33:41.172808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdaffa79f42e'
down_revision = 'dfe758c4bda5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timezone', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('timezone')

    # ### end Alembic commands ###
