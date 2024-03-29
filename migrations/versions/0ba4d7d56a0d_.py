"""empty message

Revision ID: 0ba4d7d56a0d
Revises: 
Create Date: 2019-12-10 10:25:47.830134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba4d7d56a0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wish_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wish_title', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wish_model_wish_title'), 'wish_model', ['wish_title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_wish_model_wish_title'), table_name='wish_model')
    op.drop_table('wish_model')
    # ### end Alembic commands ###
