"""empty message

Revision ID: 17aa17e7619f
Revises: 4aa43f2f0a7d
Create Date: 2024-03-19 11:28:14.120806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17aa17e7619f'
down_revision = '4aa43f2f0a7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('releases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('buy_link', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('releases', schema=None) as batch_op:
        batch_op.drop_column('buy_link')

    # ### end Alembic commands ###
