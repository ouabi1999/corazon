"""empty message

Revision ID: 75915cb94095
Revises: 76e832b3b251
Create Date: 2023-03-02 17:59:48.627306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75915cb94095'
down_revision = '76e832b3b251'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('my_table')
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    op.create_table('my_table',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='my_table_pkey')
    )
    # ### end Alembic commands ###
