"""empty message

Revision ID: 43716130a31f
Revises: bfad64684be2
Create Date: 2023-01-21 18:50:58.790652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43716130a31f'
down_revision = 'bfad64684be2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reset_password_uuid', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('reset_password_uuid')

    op.drop_table('plants')
    # ### end Alembic commands ###
