from fastapi import APIRouter
from app.database.crud import read

router = APIRouter()


@router.get("/users/", tags=["users"])
async def users_list():
    req_column = "id, user_name"
    req_table = "user"
    user_list = await read(req_column, req_table)

    data = []
    for user in user_list:
        data.append({user[0]: user[1]})
    return data
