"""agent_add_region

Revision ID: 93e9d31d40bf
Revises: 80176413d8aa
Create Date: 2017-09-28 15:01:38.944738

"""
from alembic import op
import sqlalchemy as sa
import sorna.manager.models.base
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '93e9d31d40bf'
down_revision = '80176413d8aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agents', sa.Column('region', sa.String(length=64), nullable=False, server_default='amazon/ap-northeast-2'))
    op.create_index(op.f('ix_agents_region'), 'agents', ['region'], unique=False)
    op.alter_column('keypairs', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('keypairs', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.drop_index(op.f('ix_agents_region'), table_name='agents')
    op.drop_column('agents', 'region')
    # ### end Alembic commands ###
