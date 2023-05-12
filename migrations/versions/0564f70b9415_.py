"""empty message

Revision ID: 0564f70b9415
Revises: 26d45ad99117
Create Date: 2023-05-10 17:24:05.887611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0564f70b9415'
down_revision = '26d45ad99117'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###