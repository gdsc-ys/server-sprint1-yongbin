from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def users_list():
    return [{"username": "kim"}, {"username": "lee"}, {"username": "park"}]
