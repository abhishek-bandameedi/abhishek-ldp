from sqlalchemy.orm import Session
from app.models.models import User, Post
from app.exceptions.custom import PostCreateException, UserCreateException

def create_user(db: Session, username: str):
    try:
        db_user = User(username=username)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print(f"Error creating user: {e}")
        raise UserCreateException() from e

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user_update: dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for key, value in user_update.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def patch_user(db: Session, user_id: int, user_update: dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for key, value in user_update.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()

# def create_post(db: Session, title: str, content: str, user_id: int):
#     try:
#         db_post = Post(title=title, content=content, user_id=user_id)
#         db.add(db_post)
#         db.commit()
#         db.refresh(db_post)
#         return db_post
#     except Exception as e:
#         print(f"Error creating post: {e}")
#         raise PostCreateException() from e
    

# def get_post(db: Session, post_id: int):
#     return db.query(Post).filter(Post.id == post_id).first()

# def update_post(db: Session, post_id: int, post_update: dict):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post:
#         for key, value in post_update.items():
#             setattr(db_post, key, value)
#         db.commit()
#         db.refresh(db_post)
#     return db_post

# def delete_post(db: Session, post_id: int):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post:
#         db.delete(db_post)
#         db.commit()