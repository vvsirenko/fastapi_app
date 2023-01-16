from fastapi import APIRouter

from src.database import mock_data

router = APIRouter()


@router.get("/user/{user_id}")
def get_user(user_id: int):
    return [user for user in mock_data if user.get("id") == user_id]
