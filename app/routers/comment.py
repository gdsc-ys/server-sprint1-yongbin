from fastapi import APIRouter
from app.database.crud import read

router = APIRouter()


@router.get("/posts/{post_id}/comments/", tags=["comments"])
async def comment_list(post_id: int):
    req_column = "*"
    req_table = "Comment"
    where = f"post_id={post_id}"

    comment_list = await read(req_column, req_table, where)
    data = []
    for comment in comment_list:
        user_name = await read("user_name", "user", f"id={comment[3]}")
        data.append({
            "commentId": comment[0],
            "content": comment[1],
            "writer": user_name[0][0]
        })


    return data
