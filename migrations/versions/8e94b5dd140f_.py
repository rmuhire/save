"""empty message

Revision ID: 8e94b5dd140f
Revises: d92eb5c33326
Create Date: 2017-09-04 18:28:44.273454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e94b5dd140f'
down_revision = 'd92eb5c33326'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_sg_member_contributions_sg_cycle_id', table_name='sg_member_contributions')
    op.drop_index('ix_sg_member_contributions_sg_member_id', table_name='sg_member_contributions')
    op.drop_constraint(u'sg_member_contributions_sg_member_id_fkey', 'sg_member_contributions', type_='foreignkey')
    op.drop_constraint(u'sg_member_contributions_sg_cycle_id_fkey', 'sg_member_contributions', type_='foreignkey')
    op.drop_column('sg_member_contributions', 'sg_cycle_id')
    op.drop_column('sg_member_contributions', 'sg_member_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sg_member_contributions', sa.Column('sg_member_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('sg_member_contributions', sa.Column('sg_cycle_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'sg_member_contributions_sg_cycle_id_fkey', 'sg_member_contributions', 'sg_cycle', ['sg_cycle_id'], ['id'])
    op.create_foreign_key(u'sg_member_contributions_sg_member_id_fkey', 'sg_member_contributions', 'sg_member', ['sg_member_id'], ['id'])
    op.create_index('ix_sg_member_contributions_sg_member_id', 'sg_member_contributions', ['sg_member_id'], unique=False)
    op.create_index('ix_sg_member_contributions_sg_cycle_id', 'sg_member_contributions', ['sg_cycle_id'], unique=False)
    # ### end Alembic commands ###
