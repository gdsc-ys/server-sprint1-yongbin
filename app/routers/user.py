from fastapi import APIRouter
from app.database.crud import read
from app.database.redis import write_redis, read_redis
import time

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


@router.get("/users/{user_id}", tags=["users"])
async def users_redis(user_id: int):
    start = time.time()

    user_info = await read_redis(user_id)
    if not user_info:
        print("SQL")
        table = "User"
        columns = "*"
        user = await read(columns, table, f"id = {user_id}")
        user = user[0]
        user_info = {
            user[0]: {
                "id": user[0],
                "name": user[2],
                "password": user[1],
                "email": user[3],
                "disabled": user[4]
            }
        }
        res = await write_redis(user[0], user_info)
        print(f"res:{res}")
        if res:
            print("save cache in redis success")
        else:
            print("save cache in redis FAIL")

    user_info["time"] = time.time() - start

    return user_info

