"""empty message

Revision ID: 407d26c14ff0
Revises: None
Create Date: 2016-05-31 01:04:56.391000

"""

# revision identifiers, used by Alembic.
revision = '407d26c14ff0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('status', sa.SmallInteger(), server_default='0'))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entry', 'status')
    ### end Alembic commands ###
