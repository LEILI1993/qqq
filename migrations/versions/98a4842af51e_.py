"""empty message

Revision ID: 98a4842af51e
Revises: 
Create Date: 2018-08-08 12:08:48.542233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98a4842af51e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinemas',
    sa.Column('cid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('district', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.Column('score', sa.Float(precision=3, asdecimal=1), nullable=True),
    sa.Column('hallnum', sa.String(length=100), nullable=True),
    sa.Column('servicecharge', sa.String(length=100), nullable=True),
    sa.Column('astrict', sa.String(length=100), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('cid')
    )
    op.create_index(op.f('ix_cinemas_name'), 'cinemas', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cinemas_name'), table_name='cinemas')
    op.drop_table('cinemas')
    # ### end Alembic commands ###
