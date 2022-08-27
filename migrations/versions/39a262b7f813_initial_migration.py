"""Initial migration

Revision ID: 39a262b7f813
Revises: 
Create Date: 2022-08-27 12:50:20.208704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39a262b7f813'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies_actors',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actor.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'actor_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies_actors')
    op.drop_table('movie')
    op.drop_table('actor')
    # ### end Alembic commands ###
