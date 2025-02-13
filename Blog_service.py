from Blog_repository import (
    UserRepository, NewsRepository, CommentsRepository,
    CategoriesRepository, TagsRepository, DataUserRepository
)


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def add_user(self, user_name: str, email: str, password_hash: int, profile_picture) -> str:
        """Добавляет нового пользователя"""
        return self.repository.add_user(user_name, email, password_hash, profile_picture)

    def get_users(self) -> str:
        """Получение всех пользователей"""
        return self.repository.get_users()

    def update_user(self, update_user: str) -> str:
        """изменяет имя пользователя"""
        print("Имя пользователя успешно изменено!")
        return self.repository.update_user(update_user)

    def delete_user(self, del_id: str) -> str:
        """Удаляет пользователя"""
        print("Пользователь успешно удален!")
        return self.repository.delete_user(del_id)


class CheckUserService:
    def __init__(self, repository: DataUserRepository):
        self.repository = repository

    def authorization(self, user_name: str, user_password: int) -> bool:
        """Проверка логина пароля"""
        user = self.repository.check_login(user_name)
        if user is not None:
            if user.password_hash == user_password:
                return True
            else:
                return False
        else:
            return False

    def admin(self, user_name: str) -> str or bool:
            """Админ не удаляет сам себя"""
            admin = self.repository.check_login(user_name)
            if admin is not None:
                print("Администратор не может удалить сам себя!")
                return False


class NewsService:
    def __init__(self, repository: NewsRepository):
        self.repository = repository

    def add_new(self, author_id: int, category_id: int, title: str, content: str) -> str:
        """Добавляет статью"""
        return self.repository.add_post(author_id, category_id, title, content)

    def get_title_news(self) -> str:
        """Полуение название статей"""
        return self.repository.get_title_post()

    def get_posts(self) -> str:
        """Полуение всех статей"""
        return self.repository.get_posts()

    def get_post_by_title(self, title_post: str) -> str:
        """Полуение статьи по заголовку"""
        return self.repository.get_post_by_title(title_post)

    def update_post(self, new_content:str) -> str:
        """Обновление статьи"""
        print("статья успешно изменена!")
        return self.repository.update_post(new_content)

    def delete_post(self, id: str) -> str:
        """Удаляет статью"""
        print("Статья удалена!")
        return self.repository.delete_post(id)


class CategoriesService:
    def __init__(self, repository: CategoriesRepository):
        self.repository = repository

    def add_category(self, id: int, name:str, description:str) -> str:
        """Добавляет категорию"""
        return self.repository.add_category(id, name, description)

    def get_categories(self) -> str:
        """Полуение категорий статей"""
        return self.repository.get_categories()

    def update_category(self, new_name: str) -> str:
        """Обновление названия категории"""
        print("Категория успешно изменена!")
        return self.repository.update_category(new_name)

    def delete_category(self, del_id: int) -> str:
        """Удаляет категорию"""
        print("Категория удалена!")
        return self.repository.delete_category(del_id)


class CommentsService:
    def __init__(self, repository: CommentsRepository):
        self.repository = repository

    def add_comment(self, id: int, post_id: int, user_id: int, content: str) -> str:
        """Добавление комментария"""
        return self.repository.add_comment(id, post_id, user_id, content)

    def get_comments_by_user(self, user_id: int) -> str:
        """Выводит все комментарии пользователя"""
        return self.repository.get_comments_by_user(user_id)

    def get_comment_by_post(self, post_id: int) -> str:
        """Комментарии нужной статьи"""
        return self.repository.get_comments_by_post(post_id)

    def update_comment(self, content: str) -> str:
        """Обновление комментария"""
        print("Комментарий усппешно изменен!")
        return self.repository.update_comment(content)


class TagsService:
    def __init__(self, repository: TagsRepository):
        self.repository = repository

    def add_tag(self, name: str) -> str:
        """Добавление тега"""
        return self.repository.add_tags(name)

    def get_all_tags(self) -> str:
        """Получение всех тегов"""
        return self.repository.get_all_tags()

    def update_tag(self, name: str) -> str:
        """Обновление тега"""
        print("Тег успешно изменен!")
        return self.repository.update_tag(name)

    def delete_tag(self, id):
        """Удаление тега"""
        print("Тег удален!")
        return self.repository.delete_tag(id)
