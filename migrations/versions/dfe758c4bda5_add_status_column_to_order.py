"""Add status column to Order

Revision ID: dfe758c4bda5
Revises: e2cb6e1e3e27
Create Date: 2025-03-16 01:07:27.799052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfe758c4bda5'
down_revision = 'e2cb6e1e3e27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=True))
        batch_op.alter_column('invoice_number',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=32),
               existing_nullable=True)
        batch_op.drop_constraint('order_order_number_key', type_='unique')
        batch_op.drop_column('order_number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_number', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
        batch_op.create_unique_constraint('order_order_number_key', ['order_number'])
        batch_op.alter_column('invoice_number',
               existing_type=sa.String(length=32),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.drop_column('status')

    # ### end Alembic commands ###
