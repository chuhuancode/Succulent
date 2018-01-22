"""empty message

Revision ID: cfeb88b40dc6
Revises: 
Create Date: 2018-01-20 20:33:13.946333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfeb88b40dc6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('good_name', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('introduction', sa.Text(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account', sa.String(length=120), nullable=True),
    sa.Column('nickname', sa.String(length=120), nullable=True),
    sa.Column('passwd_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('duocoin', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account'),
    sa.UniqueConstraint('email')
    )
    op.create_table('beauti_essay',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('intro', sa.String(length=1000), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('praise_num', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goods_img',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=256), nullable=True),
    sa.Column('goods', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goods'], ['goods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('context', sa.String(length=1024), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=256), nullable=True),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rid', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('praise_num', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_posts_rid'), 'posts', ['rid'], unique=False)
    op.create_table('shoppingcar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('be_user',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('be_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['be_id'], ['beauti_essay.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('beau_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('beau_esssay', sa.Integer(), nullable=True),
    sa.Column('u', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['beau_esssay'], ['beauti_essay.id'], ),
    sa.ForeignKeyConstraint(['u'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beau_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('beau_photo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['beau_photo'], ['beauti_essay.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('posts_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('posts_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopping',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('Shoppingcar_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Shoppingcar_id'], ['shoppingcar.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopping')
    op.drop_table('image')
    op.drop_table('favorite')
    op.drop_table('beau_image')
    op.drop_table('beau_comment')
    op.drop_table('be_user')
    op.drop_table('shoppingcar')
    op.drop_index(op.f('ix_posts_rid'), table_name='posts')
    op.drop_table('posts')
    op.drop_table('news_image')
    op.drop_table('news_comment')
    op.drop_table('goods_img')
    op.drop_table('beauti_essay')
    op.drop_table('users')
    op.drop_table('news')
    op.drop_table('goods')
    # ### end Alembic commands ###
