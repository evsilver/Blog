from sqlalchemy import select, update, delete
from Blog_tables import Users, News, Categories, Comments, Tags



class UserRepository:
    def __init__(self, session):
        self.session = session

    def add_user(self, user_name, email, password_hash, profile_picture) -> str:
        """Добавление пользователя в БД"""
        new_user = Users(
            user_name=user_name, email=email,
            profile_picture=profile_picture, password_hash=password_hash)
        self.session.add(new_user)
        self.session.commit()

    def get_users(self) -> str:
        """Полуение пользователей из БД"""
        all_users = select(Users)
        raw = self.session.execute(all_users)
        return raw.scalars()

    def update_user(self, update_name) -> str:
        """Изменение данных"""
        stmt = update(Users).filter_by(Users.user_name == update_name).returning(Users)
        user = self.session.execute(stmt)
        self.session.commit()
        return user.scalar_one()

    def delete_user(self, del_id):
        """Удаление пользователя"""
        stmt = delete(Users).where(Users.id == del_id)
        self.session.execute(stmt)
        self.session.commit()


class DataUserRepository:
    def __init__(self, session):
        self.session = session

    def check_login(self, user_name) -> Users | None:
        """Получение из БД имени пользователя"""
        user = select(Users).filter_by(Users.user_name == user_name)
        right_user = self.session.execute(user)
        return right_user.scalar_one_or_none()


class NewsRepository:
    def __init__(self, session):
        self.session = session

    def add_post(self, author_id, category_id, title, content) -> str:
        """Добавление статьи в БД"""
        new_post = News(author_id=author_id, category_id=category_id, title=title, content=content)
        self.session.add(new_post)
        self.session.commit()

    def get_title_post(self) -> str:
        """Получение заголовков статей из БД"""
        all_title_posts = select(News)
        raw = self.session.execute(all_title_posts)
        return raw.scalars()

    def get_posts(self):
        """Полуение всех статей"""
        all_posts = select(News).filter_by(News.content)
        raw = self.session.execute(all_posts)
        return raw.scalars()

    def get_post_by_title(self, title_post) -> str:
        """Получение статей по заголовку"""
        post_by_title = select(News).filter_by(News.content == title_post)
        raw = self.session.execute(post_by_title)
        return raw.scalars()

    def update_post(self, new_content) -> str:
        """Изменение новости"""
        stmt = update(News).filter_by(News.content == new_content)
        raw = self.session.execute(stmt)
        self.session.commit()
        return raw.scalar_one()

    def delete_post(self, del_id):
        """удаление новости"""
        stmt = delete(News).where(News.id == del_id)
        self.session.execute(stmt)
        self.session.commit()


class CategoriesRepository:
    def __init__(self, session):
        self.session = session

    def add_category(self, id, name, description) -> str:
        """Добавление категории"""
        new_category = Categories(id=id, name=name, description=description)
        self.session.add(new_category)
        self.session.commit()
        return "Новый пользователь добавлен!"

    def get_categories(self) -> str:
        """Полуение категорий"""
        stmt = select(Categories)
        raw = self.session.execute(stmt)
        return raw.scalars()

    def update_category(self, new_name) -> str:
        """Изменение категории"""
        stmt = update(Categories).filter_by(Categories.name == new_name)
        raw = self.session.execute(stmt)
        self.session.commit()
        return raw.scalar_one()

    def delete_category(self, del_id):
        """Удаление категории"""
        stmt = delete(Categories).where(Categories.id == del_id)
        self.session.execute(stmt)
        self.session.commit()


class CommentsRepository:
    def __init__(self, session):
        self.session = session

    def add_comment(self, id, post_id, user_id, content) -> str:
        """Добавление комментария"""
        new_comment = Comments(
            id=id, post_id=post_id, user_id=user_id, content=content
        )
        self.session.add(new_comment)
        self.session.commit()
        return "Комментарий добавлен!"

    def get_comments_by_user(self, user_id) -> str:
        """Все комментарии пользователя"""
        all_user_comments = select(Comments).filer_by(Comments.user_id == user_id)
        raw = self.session.execute(all_user_comments)
        self.session.commit()
        return raw.scalars()

    def get_comments_by_post(self, post_id: int) -> str:
        """все комментарии к новости"""
        all_post_comments = select(Comments).filter_by(Comments.post_id == post_id)
        raw = self.session.execute(all_post_comments)
        self.session.commit()
        return raw.scalars()

    def update_comment(self, content: str) -> str:
        """Изменение комментария"""
        stmt = update(Comments).filter_by(Comments.content == content)
        raw = self.session.execute(stmt)
        self.session.commit()
        return raw.scalar_one()

    def delete_comment(self, del_id: int) -> str:
        """удаления комментария"""
        stmt = delete(Comments).where(Comments.id == del_id)
        self.session.execute(stmt)
        self.session.commit()


class TagsRepository():
    def __init__(self, session):
        self.session = session

    def add_tags(self, name: str) -> str:
        """Добавление тего"""
        new_tag = Tags(name=name)
        self.session.add(new_tag)
        self.session.commit()
        return "Тег добавлен!"

    def get_all_tags(self) -> str:
        """Получение всех тегов"""
        all_tags = select(Tags)
        raw = self.session.execute(all_tags)
        self.session.commit()
        return raw.scalars()

    def update_tag(self, name):
        """Обновление тегов"""
        stmt = update(Tags).filter_by(Tags.name == name)
        raw = self.session.execute(stmt)
        self.session.commit()
        return raw.scalar_one()

    def delete_tag(self, name: str) -> str:
        """Удаление тега"""
        stmt = delete(Tags).where(Tags.name == name)
        self.session.execute(stmt)
        self.session.commit()

