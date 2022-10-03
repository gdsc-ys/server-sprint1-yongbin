from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from app.database.crud import read, create
from app.models.post import Post, CreatePost

router = APIRouter()


@router.get("/posts/", tags=["posts"])
async def posts_list():
    req_column = "*"
    req_table = "post"
    post_list = await read(req_column, req_table)
    data = []
    for post in post_list:
        user_name = await read("user_name", "user", f"id={post[3]}")
        data.append({
            "postId": post[0],
            "content": post[1],
            "like_num": post[2],
            "writer": user_name[0][0]
        })

    return data


@router.post("/posts/", tags=["posts"], response_model=Post)
async def posts_create(post: CreatePost):
    post_dict = post.dict()
    table = "Post"
    new_id = await create(table, post_dict)
    data = {"new_id": new_id}
    return ORJSONResponse([data])
