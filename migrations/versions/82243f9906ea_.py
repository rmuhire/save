"""empty message

Revision ID: 82243f9906ea
Revises: 06e6b0c847f6
Create Date: 2017-09-07 22:44:29.970781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82243f9906ea'
down_revision = '06e6b0c847f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member_approved_loan', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('member_loan', sa.Column('approved_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('member_loan', 'approved_date')
    op.drop_column('member_approved_loan', 'date')
    # ### end Alembic commands ###
