from fastapi import APIRouter
from app.data import database as data_database
from app.data import schemas as data_schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/{user_id}")
def get_user(user_id: int):
    return [user for user in data_database.data if user.get("id") == user_id]


@router.post("/{user_data: user_data}")
def post_user(user_data: dict):
    user_data = data_schemas.User(**user_data)
    if user_data and user_data.validate:
        data_database.data.append(user_data)
        answer = {"status": 200, "data": data_database.data}
    else:
        answer = {"status": "data not validate", "data": data_database.data}
    return answer
