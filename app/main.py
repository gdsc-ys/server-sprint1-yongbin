import uvicorn
from dataclasses import asdict
from fastapi import FastAPI
from app.common.config import conf
from app.database.conn import connect_mysql
from app.routers import root, user


def create_app():
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)

    # router
    app.include_router(root.router)
    app.include_router(user.router, tags=["user"])

    # DB_pool
    app.state.db_pool = connect_mysql(**conf_dict)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
