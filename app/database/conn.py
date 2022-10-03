from fastapi import FastAPI
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class SQLALchemy:
    def __init__(self, app: FastAPI = None, **kwargs):
        self._engine = None
        self._session = None
        if app is not None:
            self.init_app(app=app, **kwargs)

    # DB 초기화
    def init_app(self, app: FastAPI, **kwargs):
        """
        DB 초기화
        :param app:
        :param kwargs:
        :return:
        """
        database_url = kwargs.get("DB_URL")
        pool_recycle = kwargs.setdefault("DB_POOL_RECYCLE", 900)
        echo = kwargs.setdefault("DB_ECHO", True)

        self._engine = create_engine(
            database_url,
            echo=echo,
            pool_recycle=pool_recycle,
            pool_pre_ping=True,
            encoding='utf-8'
        )
        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

        # app 시작할 때 실행
        @app.on_event("startup")
        def startup():
            self._engine.connect()
            # logging.info("DB connected")

        # app 끝날 때 실행
        @app.on_event("shutdown")
        def shutdown():
            self._session.close_all()
            self._engine.dispose()
            # logging.info("DB disconnected")

    def get_db(self):
        """
        요청마다 DB 세션 유지
        :return:
        """
        if self._session is None:
            raise Exception("must be called 'init_app'")
        db_session = None
        try:
            db_session = self._session()
            yield db_session
        finally:
            db_session.close()

    @property
    def session(self):
        return self.get_db

    @property
    def engine(self):
        return self._engine


db = SQLALchemy()
Base = declarative_base()