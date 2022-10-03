from fastapi import APIRouter
from app.database.crud import read

router = APIRouter()


@router.get("/posts/", tags=["posts"])
async def posts_list():
    req_column = "*"
    req_table = "post"
    post_list = await read(req_column, req_table)
    data = []
    for post in post_list:
        user_name = await read("user_name", "user", f"id={post[3]}")
        print(user_name)
        data.append({
            "postId": post[0],
            "content": post[1],
            "like_num": post[2],
            "writer": user_name[0][0]
        })

    return data
