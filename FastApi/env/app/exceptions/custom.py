from fastapi import HTTPException, status

class NotFoundException(HTTPException):
    def __init__(self, item_name: str):
        detail = f"{item_name} not found"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class UserNotFoundException(NotFoundException):
    def __init__(self):
        super().__init__("User")

class PostNotFoundException(NotFoundException):
    def __init__(self):
        super().__init__("Post")

class PostCreateException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create post")

class UserCreateException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user")