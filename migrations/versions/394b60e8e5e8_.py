"""empty message

Revision ID: 394b60e8e5e8
Revises: 8e89cc53e18f
Create Date: 2020-03-17 15:08:28.322991

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '394b60e8e5e8'
down_revision = '8e89cc53e18f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Usuario', sa.Column('codigoConfirmacao', sa.String(length=50), nullable=False))
    op.drop_column('Usuario', 'dataNascimento')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Usuario', sa.Column('dataNascimento', mysql.DATETIME(), nullable=False))
    op.drop_column('Usuario', 'codigoConfirmacao')
    # ### end Alembic commands ###
