from dataclasses import asdict
import uvicorn
from fastapi import FastAPI
from app.common.config import conf
from app.database.conn import db

from app.routers import root, user


def create_app():
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # router
    app.include_router(root.router)
    app.include_router(user.router, tags=["user"])

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
