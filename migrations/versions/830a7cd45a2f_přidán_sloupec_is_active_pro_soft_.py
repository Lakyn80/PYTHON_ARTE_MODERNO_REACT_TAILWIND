"""Přidán sloupec is_active pro soft deletion u produktů

Revision ID: 830a7cd45a2f
Revises: a863b99f425c
Create Date: 2025-03-12 18:37:34.163487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '830a7cd45a2f'
down_revision = 'a863b99f425c'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.true()))
        # Pokud nechceš, aby byl server default zachován pro nově přidaný sloupec, můžeš jej odstranit:
        batch_op.alter_column('is_active', server_default=None)



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###
