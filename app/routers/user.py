from fastapi import APIRouter
from faker import Faker
from random import randint
from app.database.crud import read, create
import time


router = APIRouter()
fake = Faker()

@router.get("/users/", tags=["users"])
async def users_list():
    start = time.time()
    req_column = "id, user_name"
    req_table = "user"
    user_list = await read(req_column, req_table)

    data = []
    for user in user_list:
        data.append({user[0]: user[1]})
    data.insert(0, {"time": time.time() - start})
    return data


@router.get("/user/create_dummy", tags=["users"])
async def create_dummy():
    start = time.time()
    for _ in range(100000):
        rand = randint(0, 1)
        user_dict = {
            "user_name": fake.name(),
            "email": fake.email(),
            "user_password": fake.password()
        }
        if rand:
            user_dict["disabled"] = True
        else:
            user_dict["disabled"] = False
        await create("User", user_dict)

    return {"time": time.time()-start}
