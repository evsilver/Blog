from typing import Annotated
from fastapi import FastAPI, Depends, Form
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from factory import (get_user_service, get_check_user_service, get_news_service, get_category_service,
get_comment_service, get_tags_service)
from db import create_table, SessionDep
from Blog_dtos import UserResponse

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_table()


@app.post("/login")
def authorization(user_name: Annotated[str, Form()], password: Annotated[str, Form()], session: SessionDep):
    check_user_service = get_check_user_service(session)
    return check_user_service.authorization(user_name, password)

@app.post("/add_user")
def add_user(
        user_name: Annotated[str, Form()], email: Annotated[str, Form()], password_hash: Annotated[int, Form()],
        profile_picture: Annotated[str, Form()], session: SessionDep
    ):
    user_service = get_user_service(session)
    user_service.add_user(user_name, email, password_hash, profile_picture)

@app.get("/get_users", response_model=list[UserResponse])
def get_users(session: SessionDep):
    user_service = get_user_service(session)
    return user_service.get_users()

@app.put("/update_user", response_model=list[UserResponse])
def update_user(update_user: Annotated[str, Form()], session: SessionDep):
    user_service = get_user_service(session)
    user_service.update_user(update_user)

@app.delete("/delete_user")
def delete_user(id: Annotated[int, Form()], session: SessionDep):
    user_service = get_user_service(session)
    user_service.delete_user(id)

@app.post("/add_news")
def add_news(
        author_id: Annotated[int, Form()], category_id: Annotated[int, Form()],
        title: Annotated[str, Form()], content: Annotated[str, Form()], session: SessionDep
    ):
    news_service = get_news_service(session)
    news_service.add_new(author_id, category_id, title, content)

@app.get("/get_news")
def get_news(session: SessionDep):
    news_service = get_news_service(session)
    news_service.get_posts()

@app.get("/get_news's_title")
def get_title(session: SessionDep):
    news_service = get_news_service(session)
    news_service.get_title_news()

@app.get("/get_post_by_title")
def get_post_by_title(title_post: Annotated[str, Form()], session: SessionDep):
    news_service = get_news_service(session)
    news_service.get_title_news(title_post)

@app.put("/update_new")
def update_new(new_content: Annotated[str, Form()], session: SessionDep):
    news_service = get_news_service(session)
    news_service.update_post(new_content)

@app.delete("/delete_post")
def delete_post(id: Annotated[int, Form()], session: SessionDep):
    news_service = get_news_service(session)
    news_service.delete_post(id)

@app.post("/add_category")
def add_category(
        id: Annotated[int, Form()], name: Annotated[str, Form()],
        description: Annotated[str, Form()], session: SessionDep):
    category_service = get_category_service(session)
    category_service.add_category(id, name, description)

@app.get("/get_categories")
def get_categories(session: SessionDep):
    category_service = get_category_service(session)
    category_service.get_categories()

@app.put("/update_category")
def update_category(name: Annotated[str, Form()], session: SessionDep):
    category_service = get_category_service(session)
    category_service.update_category(name)

@app.delete("/delete_category")
def delete_category(id: Annotated[int, Form()], session: SessionDep):
    category_service = get_category_service(session)
    category_service.delete_category(id)

@app.post("/add_comment")
def add_comment(
        id: Annotated[int, Form()], post_id: Annotated[int, Form()],
        user_id: Annotated[int, Form()], content: Annotated[str, Form()], session: SessionDep):
    comments_service = get_comment_service(session)
    comments_service.add_comment(id, post_id, user_id, content)

@app.get("/get_comments")
def get_comments(session: SessionDep):
    comments_service = get_comment_service(session)
    comments_service.get_comments_by_user()

@app.get("/get_comments_by_post")
def get_comments_by_post(post_id: Annotated[int, Form()], session: SessionDep):
    comments_service = get_comment_service(session)
    comments_service.get_comment_by_post(post_id)

@app.put("/update_comment")
def update_comment(content: Annotated[str, Form()], session: SessionDep):
    comments_service = get_comment_service(session)
    comments_service.update_comment(content)

@app.post("/add_tag")
def add_tag(name: Annotated[str, Form()], session: SessionDep):
    tags_service = get_tags_service(session)
    tags_service.add_tag(name)

@app.get("/get_tags")
def get_tags(session: SessionDep):
    tags_service = get_tags_service(session)
    tags_service.get_all_tags()

@app.put("/update_tag")
def update_tag(name: Annotated[str, Form()], session: SessionDep):
    tags_service = get_tags_service(session)
    tags_service.update_tag(name)

@app.delete("/delete_tag")
def delete_tag(id: Annotated[int, Form()], session: SessionDep):
    tags_service = get_tags_service(session)
    tags_service.delete_tag(id)