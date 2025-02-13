import sqlalchemy as sq
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    __tableargs__ = {
        'comment': 'данные пользователей'
    }
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column()
    password_hash: Mapped[int] = mapped_column()
    profile_picture: Mapped[str] = mapped_column()
    created_at: Mapped[sq.Date] = mapped_column(sq.TIMESTAMP(timezone=True), server_default=sq.func.now())

class News(Base):
    __tablename__ = 'news'
    __tableargs__ = {
        'comment': 'данные поста'
    }
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(sq.ForeignKey('users.id'))
    category_id: Mapped[int] = mapped_column(sq.ForeignKey('categories.id'))
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    created_at: Mapped[sq.Date] = mapped_column(sq.TIMESTAMP(timezone=True), server_default=sq.func.now())
    updated: Mapped[sq.Date] = mapped_column(sq.TIMESTAMP(timezone=True), server_default=sq.func.now())
    is_draft: Mapped[bool] = mapped_column(default=True)

class Categories(Base):
    __tablename__ = 'categories'
    __tableargs__ = {
        'comment': 'категории'
    }
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

class Comments(Base):
    __tablename__ = 'comments'
    __tableargs__ = {
        'comment': 'комментарии'
    }
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(sq.ForeignKey('news.id'))
    user_id: Mapped[int] = mapped_column(sq.ForeignKey('users.id'))
    content: Mapped[str] = mapped_column()
    created_at: Mapped[sq.Date] = mapped_column(sq.TIMESTAMP(timezone=True), server_default=sq.func.now())
    is_approved: Mapped[bool] = mapped_column(default=True)

class Tags(Base):
    __tablename__ = 'tags'
    __tableargs__ = {
        'comment': 'теги'
    }
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

class TagsPosts(Base):
    __tablename__ = 'tagsposts'
    __tableargs__ = {
        'comment': 'связи'
    }
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(sq.ForeignKey('news.id'))
    tag_id: Mapped[int] = mapped_column(sq.ForeignKey('tags.id'))

