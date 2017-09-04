"""empty message

Revision ID: d92eb5c33326
Revises: 59a0d471322b
Create Date: 2017-09-04 18:23:13.025731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd92eb5c33326'
down_revision = '59a0d471322b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sg_member_contributions', sa.Column('sg_cycle_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_sg_member_contributions_sg_cycle_id'), 'sg_member_contributions', ['sg_cycle_id'], unique=False)
    op.create_foreign_key(None, 'sg_member_contributions', 'sg_cycle', ['sg_cycle_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sg_member_contributions', type_='foreignkey')
    op.drop_index(op.f('ix_sg_member_contributions_sg_cycle_id'), table_name='sg_member_contributions')
    op.drop_column('sg_member_contributions', 'sg_cycle_id')
    # ### end Alembic commands ###
