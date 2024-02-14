import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.db.session import get_db
from main import app

DATABASE_URL = 'mysql+pymysql://student:student@localhost:3306/sql_app'

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture
def override_get_db():
    """
    Override the get_db dependency to use the testing database session.
    """
    return TestingSessionLocal()


@pytest.fixture
async def client():
    """
    Create an async httpx client for testing.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


def test_create_user_endpoint(client, override_get_db):
    response = client.post("/users/", json={"username": "test_user"})
    assert response.status_code == 201
    data = response.json()
    assert "user" in data
    assert "token" in data


def test_read_user_endpoint(client, override_get_db):
    # Create a test user
    create_response = client.post("/users/", json={"username": "test_user"})
    assert create_response.status_code == 201
    user_id = create_response.json()["user"]["id"]

    # Test reading the user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "username" in data
    assert data["id"] == user_id


def test_update_user_endpoint(client, override_get_db):
    # Create a test user
    create_response = client.post("/users/", json={"username": "test_user"})
    assert create_response.status_code == 201
    user_id = create_response.json()["user"]["id"]

    # Test updating the user
    update_response = client.put(f"/users/{user_id}", json={"username": "updated_user"})
    assert update_response.status_code == 200
    data = update_response.json()
    assert "id" in data
    assert "username" in data
    assert data["id"] == user_id
    assert data["username"] == "updated_user"


def test_delete_user_endpoint(client, override_get_db):
    # Create a test user
    create_response = client.post("/users/", json={"username": "test_user"})
    assert create_response.status_code == 201
    user_id = create_response.json()["user"]["id"]

    # Test deleting the user
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 204

    # Test that the user is deleted
    read_response = client.get(f"/users/{user_id}")
    assert read_response.status_code == 404







# from main import app
# import pytest
# from httpx import AsyncClient 

# @pytest.mark.asyncio
# async def test_create_user():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("/users/", json={"username": "test_user"})
#     assert response.status_code == 201
#     assert "user" in response.json()
#     assert "token" in response.json()

# @pytest.mark.asyncio
# async def test_read_user():
#     # Assuming there is a user with ID 1 in the database
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/users/1")
#     assert response.status_code == 200
#     assert "id" in response.json()
#     assert "username" in response.json()

# @pytest.mark.asyncio
# async def test_update_user():
#     # Assuming there is a user with ID 1 in the database
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.put("/users/1", json={"username": "updated_username"})
#     assert response.status_code == 200
#     assert "id" in response.json()
#     assert "username" in response.json()
#     assert response.json()["username"] == "updated_username"

# @pytest.mark.asyncio
# async def test_delete_user():
#     # Assuming there is a user with ID 1 in the database
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.delete("/users/1")
#     assert response.status_code == 204
#     assert response.text == ""