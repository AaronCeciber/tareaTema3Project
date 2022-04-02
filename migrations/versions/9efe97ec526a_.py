"""empty message

Revision ID: 9efe97ec526a
Revises: 
Create Date: 2022-04-02 20:09:56.990598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9efe97ec526a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('dni', sa.String(length=10), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('apellidos', sa.String(length=50), nullable=True),
    sa.Column('imagen', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('dni')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('apellidos', sa.String(length=50), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('cliente')
    # ### end Alembic commands ###