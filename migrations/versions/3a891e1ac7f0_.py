"""empty message

Revision ID: 3a891e1ac7f0
Revises:
Create Date: 2017-07-12 13:39:30.330692

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2.types import Geography


# revision identifiers, used by Alembic.
revision = '3a891e1ac7f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search_term', sa.String(length=139), nullable=True),
    sa.Column('twitter_id', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('text', sa.String(length=140), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('location', Geography(geometry_type='POINT', srid=4326), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('twitter_id')
    )
    op.create_index(op.f('ix_tweets_text'), 'tweets', ['text'], unique=False)
    op.create_index(op.f('ix_tweets_user'), 'tweets', ['user'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tweets_user'), table_name='tweets')
    op.drop_index(op.f('ix_tweets_text'), table_name='tweets')
    op.drop_table('tweets')
    # ### end Alembic commands ###
