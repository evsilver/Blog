from Blog_repository import DataUserRepository, NewsRepository, CommentsRepository, \
    CategoriesRepository, TagsRepository, UserRepository
from Blog_service import CheckUserService, NewsService, CommentsService, CategoriesService, TagsService, UserService


def get_check_user_service(session):
    return CheckUserService(DataUserRepository(session))

def get_user_service(session):
    return UserService(UserRepository(session))

def get_news_service(session):
    return NewsService(NewsRepository(session))


def get_category_service(session):
    return CategoriesService(CategoriesRepository(session))


def get_comment_service(session):
    return CommentsService(CommentsRepository(session))


def get_tags_service(session):
    return TagsService(TagsRepository(session))
