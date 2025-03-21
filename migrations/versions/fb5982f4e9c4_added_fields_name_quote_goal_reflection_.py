"""Added fields: name, quote, goal, reflection to User model

Revision ID: fb5982f4e9c4
Revises: d6c83ea62478
Create Date: 2025-01-31 15:29:17.641575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb5982f4e9c4'
down_revision = 'd6c83ea62478'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('quote', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('goal', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('reflection', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('reflection')
        batch_op.drop_column('goal')
        batch_op.drop_column('quote')
        batch_op.drop_column('name')

    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
