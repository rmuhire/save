"""empty message

Revision ID: 7ddff9ce6478
Revises: 5a11bb2f4c74
Create Date: 2017-09-08 16:03:49.061422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ddff9ce6478'
down_revision = '5a11bb2f4c74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('saving_group', sa.Column('status', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('saving_group', 'status')
    # ### end Alembic commands ###
