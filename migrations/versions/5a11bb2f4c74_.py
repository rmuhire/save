"""empty message

Revision ID: 5a11bb2f4c74
Revises: 6c9382fcd6ce
Create Date: 2017-09-08 12:50:39.134436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a11bb2f4c74'
down_revision = '6c9382fcd6ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member_loan', sa.Column('approve_date', sa.DateTime(), nullable=True))
    op.add_column('member_loan', sa.Column('date_payment', sa.DateTime(), nullable=True))
    op.add_column('member_loan', sa.Column('initial_date_repayment', sa.Integer(), nullable=True))
    op.drop_column('member_loan', 'date_repayment')
    op.drop_column('member_loan', 'approved_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member_loan', sa.Column('approved_date', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('member_loan', sa.Column('date_repayment', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('member_loan', 'initial_date_repayment')
    op.drop_column('member_loan', 'date_payment')
    op.drop_column('member_loan', 'approve_date')
    # ### end Alembic commands ###
