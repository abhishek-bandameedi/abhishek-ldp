# from typing import List
# from fastapi import FastAPI,HTTPException,Depends,status
# from pydantic import BaseModel
# import models
# from database import engine,SessionLocal
# from sqlalchemy.orm import Session
# from exceptions import UserNotFoundException, PostNotFoundException, PostCreateException, UserCreateException

# app=FastAPI()

# # Creating database tables based on the models using the SQLAlchemy engine
# models.Base.metadata.create_all(bind=engine)

# class PostBase(BaseModel):
#     title:str
#     content:str
#     user_id:int

# class UserBase(BaseModel):
#     username:str

# class UserUpdate(BaseModel):
#     username: str = None

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # create post
# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# async def create_post(post:PostBase,db:Session=Depends(get_db)):
#     try:
#         db_post=models.Post(**post.dict())
#         db.add(db_post)
#         db.commit()
#         db.refresh(db_post)
#         return db_post
#     except Exception as e:
#         print(f"Error creating post: {e}")
#         raise PostCreateException from e

# # Read post
# @app.get("/posts/{post_id}",status_code=status.HTTP_200_OK)
# async def read_posts(post_id:int,db:Session=Depends(get_db)):
#     post=db.query(models.Post).filter(models.Post.id==post_id).first()
#     if post is None:
#         raise PostNotFoundException()
#     return post

# # Create user
# @app.post("/users/",status_code=status.HTTP_201_CREATED)
# async def create_user(user:UserBase,db:Session=Depends(get_db)):
#     try:
#         db_user=models.User(**user.dict())
#         db.add(db_user)
#         db.commit()
#         db.refresh(db_user)
#         return db_user
#     except Exception as e:
#         print(f"Error creating user: {e}")
#         raise UserCreateException() from e


# # Read user
# @app.get("/users/{user_id}",status_code=status.HTTP_200_OK)
# async def read_user(user_id:int,db:Session=Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id==user_id).first()
#     if user is None:
#         raise UserNotFoundException()
#     return user


# # update user by id
# @app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
# async def update_user(user_id: int, user: UserBase, db: Session = Depends(get_db)):
#     db_user = db.query(models.User).filter(models.User.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     for key, value in user.dict().items():
#         setattr(db_user, key, value)

#     db.commit()
#     db.refresh(db_user)
#     return db_user

# # Partial update (PATCH) for a user by ID
# @app.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
# async def patch_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
#     db_user = db.query(models.User).filter(models.User.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     for key, value in user_update.dict(exclude_unset=True).items():
#         setattr(db_user, key, value)

#     db.commit()
#     db.refresh(db_user)
#     return db_user

# # Delete a user by ID
# @app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = db.query(models.User).filter(models.User.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     db.delete(db_user)
#     db.commit()
#     return None


# # Update a post by ID
# @app.put("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def update_post(post_id: int, post: PostBase, db: Session = Depends(get_db)):
#     db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")

#     for key, value in post.dict().items():
#         setattr(db_post, key, value)

#     db.commit()
#     db.refresh(db_post)
#     return db_post

# # Delete a post by ID
# @app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_post(post_id: int, db: Session = Depends(get_db)):
#     db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")

#     db.delete(db_post)
#     db.commit()
#     return None

from fastapi import FastAPI
from app.controllers.api import router as api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)