from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.crud import create_user, get_user,update_user,delete_user
from app.exceptions.custom import UserNotFoundException, PostNotFoundException, PostCreateException, UserCreateException
from app.jwt.jwt import create_access_token
from app.models.models import PostBase,UserUpdate 

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user_with_token(username: str, db: Session = Depends(get_db)):
    user = create_user(db, username)
    token = create_access_token(data={"sub": user.id})
    return {"user": user, "token": token}



# Read user
@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise UserNotFoundException()
    return user

# Update user by ID
@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user_endpoint(
    user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)
):
    db_user = update_user(db, user_id, user_update.dict())
    if db_user is None:
        raise UserNotFoundException()
    return db_user

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    return user