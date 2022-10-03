from dataclasses import asdict
from fastapi import FastAPI
from app.common.config import conf
from app.routers import root, user, post, comment
import aiomysql


conf = conf()
app = FastAPI()
conf_dict = asdict(conf)


# router
app.include_router(root.router)
app.include_router(user.router, tags=["users"])
app.include_router(post.router, tags=["posts"])
app.include_router(comment.router, tags=["comments"])


# DB_connect
@app.on_event("startup")
async def connect_mysql():
    app.state.db_pool = await aiomysql.create_pool(host=conf_dict['DB_HOST'], port=int(conf_dict['DB_PORT']),
                                      user=conf_dict['DB_USER'], password=conf_dict['DB_PW'],
                                      db=conf_dict['DB_NAME'], autocommit=False, minsize=10, maxsize=40)